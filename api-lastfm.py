import keyLastfm
import requests
import json

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

# Function
def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': keyLastfm.USER_AGENT}

    params = {
        'api_key': keyLastfm.API_KEY,
        'format': 'json',
        'method': payload,
    }

    r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=params)

    print(r.status_code)

lastfm_get('chart.gettopartists')
