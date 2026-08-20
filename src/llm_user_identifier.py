import os
from mistralai import Mistral
from dotenv import load_dotenv
from pathlib import Path
import logging

load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

log = logging.getLogger(__name__)

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
MODEL=os.getenv("MISTRAL_MODEL")
TEMPERATURE = float(os.getenv("LLM_TEMPERATURE"))
MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS"))

def identify_person(user: dict) -> str:
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    nationality = user["nat"]
    age = user["dob"]["age"]

    prompt = f"""
    I have a person with the following details:
    - Name: {first_name} {last_name}
    - Nationality: {nationality}
    - Age: {age}
    Who could this person be? Give a brief description.Keep it to 2-3 sentences maximum."""

    log.info(f"Identifying person: {first_name} {last_name}")

    chat_completion = client.chat.complete(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=MODEL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    return chat_completion.choices[0].message.content