import requests
import api_key
from datetime import date, timedelta

# today = date.today()

# todayWordNik = today - timedelta(days=1)

# query = {"date": todayWordNik, "api_key": api_key.api_key}

# response = requests.get(
#     "https://api.wordnik.com/v4/words.json/wordOfTheDay", params=query
# )

# wordDict = response.json()

def getwordDict():
    today = date.today()

    todayWordNik = today - timedelta(days=1)

    query = {"date": todayWordNik, "api_key": api_key.api_key}

    response = requests.get(
        "https://api.wordnik.com/v4/words.json/wordOfTheDay", params=query
    )

    wordDict = response.json()

    return wordDict

wordDict = getwordDict()

def getWord (wordDict):
    word = wordDict["word"]
    
    return word

def getDefinitions (wordDict):
    definitions = []
    for each in wordDict["definitions"]:
        definitions.append(each)

    # For cases that have multiple definitions
    source = [] 
    text = []

    for each in definitions:
        source.append(each["source"])
        text.append(each["text"])
    
    return source,text

def getExamples (wordDict):
    examples = []
    for each in wordDict["examples"]:
        examples.append(each)
    
    return examples

def getpublishedDate (wordDict):
    publishedDate = wordDict["pdd"]

    return publishedDate

def getNote (wordDict):
    note = wordDict["note"]

    return note

print(wordDict)

example = getExamples(wordDict)
print("1")
print(example)
print("2")