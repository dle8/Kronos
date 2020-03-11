from googleapiclient.discovery import build
from src.main.config import config
from collections import defaultdict


def fetch_url_metadata(search_term, **kwargs):
    # TODO: use regex to only return needed field
    # Regex for pagemap.metatags to find date published

    service = build("customsearch", "v1", developerKey=config.GOOGLE_CUSTOM_SEARCH_API_KEY)
    res = service.cse().list(q=search_term, cx=config.GOOGLE_CUSTOM_SEARCH_CSE_ID, **kwargs).execute()
    urls_metadata = []
    for item in res['items']:
        current_item = defaultdict(dict)
        current_item['title'] = item['title']
        current_item['link'] = item['link']
        current_item['thumbnail'] = item['pagemap']['cse_thumbnail']
        current_item['snippet'] = item['snippet']
        urls_metadata.append(current_item)
    return urls_metadata
