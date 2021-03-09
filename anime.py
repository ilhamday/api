import requests
import json

# response = requests.get('https://api.jikan.moe/v3/anime/1/episodes')
parameters = {
    'q': 'Black Clover',
    'page': 1,
}
response = requests.get('https://api.jikan.moe/v3/search/manga', params=parameters)

print(response.url)
print(response.status_code)
# # print(response.json())
text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)