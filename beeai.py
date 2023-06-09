import requests
import api_key
from datetime import date, timedelta
import openai

def generateHive(word):
    openai.api_key = api_key.openai_api_key
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt= """Write a 50 word narrative story for and with the word '{}'""".format(
        word.capitalize()),
            max_tokens=200,
            temperature=0.6,
        )
    
    # print(response.choices[0].text)
    return response.choices[0].text
    

def getwordDict():
    today = date.today()

    todayWordNik = today - timedelta(days=1)

    query = {"date": todayWordNik, "api_key": api_key.wordnik_api_key}

    response = requests.get(
        "https://api.wordnik.com/v4/words.json/wordOfTheDay", params=query
    )

    wordDict = response.json()

    return wordDict

wordDict = getwordDict()

def getWord (wordDict):
    word = wordDict["word"]
    word = word.capitalize()
    
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