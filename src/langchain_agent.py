import logging
import os
import random
#import time
from dotenv import load_dotenv
from pathlib import Path
from langchain_mistralai import ChatMistralAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate

load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

log = logging.getLogger(__name__)

UNKNOWN_RESPONSES = [
    "I couldn't find any reliable information about this person.",
    "This person appears to be a private individual with no public record.",
    "My search didn't return any relevant results for this person.",
    "I don't have enough information to determine their notable work.",
    "This person doesn't seem to have a public profile I can find.",
]

MAX_ITERATIONS = int(os.getenv("AGENT_MAX_ITERATIONS"))
MAX_EXECUTION_TIME = int(os.getenv("AGENT_MAX_EXECUTION_TIME"))
#SLEEP_TIME = int(os.getenv("AGENT_SLEEP_TIME"))
TEMPERATURE = float(os.getenv("LLM_TEMPERATURE"))
MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS"))

llm = ChatMistralAI(
    api_key=os.getenv("MISTRAL_API_KEY"),
    model=os.getenv("MISTRAL_MODEL"),
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS
)

tools = [WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())]

prompt = PromptTemplate.from_template("""
You are a research assistant. Your job is to find the best work done by a person.

You have access to the following tools:
{tools}

Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Question: {input}
Thought: {agent_scratchpad}
""")

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False,
    max_iterations=MAX_ITERATIONS,
    max_execution_time=MAX_EXECUTION_TIME,
    handle_parsing_errors=True
)

def find_best_work(person_name: str, description: str) -> str:
    log.info(f"Finding best work for: {person_name}")

    #time.sleep(SLEEP_TIME)

    unknown_response = random.choice(UNKNOWN_RESPONSES)

    query = f"""
    Find the best and most notable work done by {person_name}.
    Here is what we know about them: {description}
    Give a detailed summary of their best achievements.
    
    IMPORTANT RULES:
    - If you cannot find any reliable information → respond with exactly: "{unknown_response}"
    - If the search results don't match this person → respond with exactly: "{unknown_response}"
    - If this appears to be a private individual → respond with exactly: "{unknown_response}"
    - Do NOT make up or guess achievements
    - Only report what you actually found in search results
    """

    try:
        result = agent_executor.invoke({"input": query})
        return result["output"]
    except Exception as e:
        log.error(f"Agent failed for {person_name}: {e}")
        return random.choice(UNKNOWN_RESPONSES)