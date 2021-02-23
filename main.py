import requests

parameter = {'rel_rhy': 'jungle'}
request = requests.get('https://api.datamuse.com/words', parameter)

# print(request.text)
print(request.status_code)

word_json = request.json()

for wj in word_json:
    print(f'The word match: {wj["word"]}')    
    # print(wj)

print(f'The first match: {word_json[0]["word"]}')
print(word_json)
# people = requests.get('http://api.open-notify.org/astros.json')
# print(people.text)