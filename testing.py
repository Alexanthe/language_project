# from curses import keyname
import requests
import api_key
from datetime import date, timedelta

api_key.api_key

today = date.today()

todayWordNik = today - timedelta(days=1)

query = {"date": todayWordNik, "api_key": api_key.api_key}

response = requests.get(
    "https://api.wordnik.com/v4/words.json/wordOfTheDay", params=query
)

wordDict = response.json()

print(wordDict)

print(wordDict["word"])
print(wordDict["definitions"])  # Get list len and loop through
print(wordDict["examples"])  # Get list len and loop through
print(wordDict["pdd"])
print(wordDict["note"])


# query = {
#     "hasDictionaryDef": True,
#     "api_key": api_key.api_key,
#     "includePartOfSpeech": True,
#     "excludePartOfSpeech": True,
#     "maxCorpusCount": -1,
#     "minDictionaryCount": 1,
#     "maxDictionaryCount": -1,
#     "minLength": 5,
#     "maxLength": -1
# }

# response = requests.get(
#     "https://api.wordnik.com/v4/words.json/randomWord", params=query
# )

# wordsDict = response.json()

# # wordsDict = {"id": 0, "word": "corner"}  # Example

# word = wordsDict["word"]

# print(word)

# query = {"useCanonical": True, "api_key": api_key.api_key}

# response = requests.get(
#     "https://api.wordnik.com/v4/word.json/" + word + "/topExample", params=query
# )

# wordExample = response.json()

# print(wordExample)


# query = {'lat':'45', 'lon':'180'}
# response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
# print(response.json())
