import keyLastfm
import requests
import json

headers = {
    'user-agent': keyLastfm.USER_AGENT
}

payload = {
    'api_key': keyLastfm.API_KEy,
    'method': 'chart.gettopartists',
    'format': 'json'
}

#  /2.0/?method=chart.gettopartists&api_key=YOUR_API_KEY&format=json

r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)

print(r.status_code)