# import json
# from googleapiclient.discovery import build
#
# my_api_key = 'AIzaSyAmmXUHk_1Ogd2g-l5fkHg6tGHpTskxTSo'
# my_cse_id = '004633013588841260401:xhqsuqmjfa7'
#
#
# def google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     return res
#
#
# # sort='date:r:yyyymmdd:yyyymmdd')
# result = google_search("facebook stock", my_api_key, my_cse_id, start=1, sort='date:r:20170101:20180303')
# with open('search.json', 'w') as fo:
#     json.dump(result, fo, indent=2)
