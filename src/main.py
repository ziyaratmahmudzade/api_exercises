from data_fetcher import fetch_users
import logging
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

if __name__=="__main__":
    data=fetch_users()
    print(json.dumps(data, indent=2))