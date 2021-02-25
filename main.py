import requests
import json
from datetime import datetime

# API that doesn't require authentication

# Show how many people in space
# response = requests.get('http://api.open-notify.org/astros.json')

# latitude & longitude for Yogyakarta city
parameters = {
    'lat': -7.79,
    'lon': 110.37,
}

# show the next times that the international space 
# station will pass over a given location on the earth (Yogyakarta city)
response = requests.get('http://api.open-notify.org/iss-pass.json', params=parameters)

print(response.status_code)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# jprint(response.json())

# Extract the pass times
pass_times = response.json()['response']
jprint(pass_times)

# Extract the risetime values
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes) # the format of the result known as timestamp or epoch

# Convert the timestamp to undestand times
times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)