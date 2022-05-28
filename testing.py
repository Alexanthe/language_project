import requests
import api_key

api_key.api_key
hasDictionaryDef = "true"


query = {
    "hasDictionaryDef": True,
    "api_key": api_key.api_key,
    "maxCorpusCount": -1,
    "minDictionaryCount": 1,
    "minLength": 5,
    "maxLength": -1,
}
print(query.keys())

response = requests.get(
    "https://api.wordnik.com/v4/words.json/randomWord", params=query
)

print(response.json())

"""
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())
"""
print(response.json())

# GET https://wordsapiv1.p.mashape.com/words/{word}
# https://www.macvendorlookup.com/api
