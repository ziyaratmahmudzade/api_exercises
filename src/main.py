from data_fetcher import fetch_users
from format_users import filter_users
import logging
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

if __name__=="__main__":
    data=fetch_users()
    #print(json.dumps(data, indent=2))

    if data is None:
        log.error("Failed to retrieve users from API")
    else:
        names = filter_users(data)

        print("[")
        for name in names:
            print(f" '{name}', ")
        print("]")