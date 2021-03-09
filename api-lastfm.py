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

    # Add API ket and format to the payload
    payload['api_key'] = keyLastfm.API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response

r = lastfm_get({
    'method': 'chart.gettopartists'
})

print(r.status_code)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# jprint(r.json())
jprint(r.json()['artists']['@attr'])
