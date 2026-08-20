import os
import requests
import logging
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path = Path(__file__).parent.parent / ".env")
log = logging.getLogger(__name__) 

URL = os.getenv("API_URL")
RESULTS = os.getenv("API_RESULTS")

def fetch_users() -> dict | None:
    try:
        response = requests.get(URL, params={"results": RESULTS})
        response.raise_for_status()
        data=response.json()
        return data
    except requests.exceptions.RequestException as e:
        log.error(f"FAILED to FETCH Users: {e}")
        return None