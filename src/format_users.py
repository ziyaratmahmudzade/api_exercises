import logging

log=logging.getLogger(__name__)

def filter_users(data: dict) -> list[str]:
    if "results" not in data:
        log.warning("missing results key")
        return []

    names = []
    for user in data["results"]:
        birth_year = int(user["dob"]["date"][:4])

        if birth_year > 2000:
            continue

        first_name = user["name"]["first"]
        last_name = user ["name"]["last"]
        full_name = first_name +" "+ last_name
        names.append(full_name)
        
    log.info("Filtered user list is ready")
    return names