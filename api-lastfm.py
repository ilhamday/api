import keyLastfm
import requests
import json
import requests_cache
import time
from IPython.core.display import clear_output

requests_cache.install_cache()

# headers = {
#     'user-agent': keyLastfm.USER_AGENT
# }
#
# payload = {
#     'api_key': keyLastfm.API_KEY,
#     'method': 'chart.gettopartists',
#     'format': 'json'
# }
#
# #  /2.0/?method=chart.gettopartists&api_key=YOUR_API_KEY&format=json
#
# r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
#
# print(r.status_code)

# My Function --------------
# def lastfm_get(payload):
#     # define headers and URL
#     headers = {'user-agent': keyLastfm.USER_AGENT}
#
#     params = {
#         'api_key': keyLastfm.API_KEY,
#         'format': 'json',
#         'method': payload,
#     }
#
#     response = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=params)
#
#     return response
#
# r = lastfm_get('chart.gettopartists')
# ---------------------------

def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': keyLastfm.USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload['api_key'] = keyLastfm.API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


responses = []

page = 1
total_pages = 10 # this is just a dummy number so the loop starts

while page <= total_pages:
    payload = {
        'method': 'chart.gettopartists',
        'limit': 500,
        'page': page
    }

    # print some output
    print(f'Requesting page {page}/{total_pages}')
    # clear the output to make things neater
    clear_output(wait = True)

    # make the API call
    response = lastfm_get(payload)

    # if get an error, print the response and halt the loop
    if response.status_code != 200:
        print(response.text)
        break

    # extract pagination info
    page = int(response.json()['artists']['@attr']['page'])
    total_pages = int(response.json()['artists']['@attr']['totalPages'])

    # append response
    responses.append(response)

    # if it's not a cached result, sleep
    if not getattr(response, 'from_cache', False):
        time.sleep(1.25)

    # increment the page number
    page += 1
