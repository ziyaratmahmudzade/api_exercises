import logging
from data_fetcher import fetch_users
from llm_user_identifier import identify_person
from langchain_agent import find_best_work

logging.basicConfig(level=logging.INFO)

# suppress noisy loggers
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("langchain_mistralai").setLevel(logging.WARNING)
logging.getLogger("langchain_mistralai").setLevel(logging.ERROR)

log= logging.getLogger(__name__)

if __name__ == "__main__":
    data = fetch_users()

    if data is None:
        log.error("Failed to fetch users from API")
    else:
        users = data["results"]

        for user in users:
            first_name = user["name"]["first"]
            last_name = user["name"]["last"]
            full_name = f"{first_name} {last_name}"

            print(f"Person: {full_name}")

            description = identify_person(user)
            print(f"\nWho are they?\n{description}")

            print(f"\nBest work:")
            best_work = find_best_work(full_name, description)
            print(best_work)

        log.info("Done!")