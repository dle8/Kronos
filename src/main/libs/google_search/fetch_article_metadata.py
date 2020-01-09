from googleapiclient.discovery import build
from src.main.config import config


def fetch_url_metadata(search_term, **kwargs):
    # Todo: use regex to only return needed field
    service = build("customsearch", "v1", developerKey=config.GOOGLE_CUSTOM_SEARCH_API_KEY)
    res = service.cse().list(q=search_term, cx=config.GOOGLE_CUSTOM_SEARCH_CSE_ID, **kwargs).execute()
    return res