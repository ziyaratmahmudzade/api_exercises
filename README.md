## API Exercises and LLM integration
Fetches random users from randomuser.me, filters them by birth year, identifies them with Mistral AI, and researches their best work using a LangChain agent.

## Project Structure
```
src/
├── data_fetcher.py         ← fetches users from API
├── format_users.py         ← filters users born after 2000
├── llm_user_identifier.py  ← identifies person via Mistral AI
├── langchain_agent.py      ← researches best work via LangChain
├── main.py                 ← exercises 1, 2, 3
├── main_4.py               ← exercise 4 (LLM identification)
└── main_5.py               ← exercise 5 (LangChain agent)
tests/
└── test_formatter.py       ← unit tests
.env.example                ← config template
requirements.txt            ← dependencies
```
## Setup
```bash
git clone https://github.com/ziyaratmahmudzade/api_exercises.git
cd api_exercises
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env         # fill in your values
```
## Usage
```bash
cd src
python main.py      # exercises 1, 2, 3
python main_4.py    # exercise 4 - LLM identification
python main_5.py    # exercise 5 - LangChain agent
```
## Testing
pytest tests/ -v

## Postman Testing
The API was manually tested using Postman before implementation.
GET https://randomuser.me/api/?results=20
Expected response: 200 OK with JSON body containing results array.

## Architecture
```
randomuser.me API
      ↓
data_fetcher.py        ← fetch
      ↓
format_users.py        ← filter
      ↓
llm_user_identifier.py ← identify (Mistral AI)
      ↓
langchain_agent.py     ← research (LangChain)
      ↓
Final output
```

## Best Practices Applied
- Virtual environment for dependency isolation
- `.env` file for secrets and configuration
- `.env.example` as template for reviewers
- Error handling with `try/except`
- Logging instead of `print()`
- Rate limiting to control API limits
- Low temperature (0.1) to reduce hallucinations and return factual responses instead of creative ones
- Max tokens to control cost
- CI/CD pipeline with feature branches and pull requests
- pytest test cases