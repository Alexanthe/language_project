from flask import Flask, render_template
from beeai import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    #Retrive WordDict
    wordDict = getwordDict()
    word = getWord(wordDict)
    source, text  = getDefinitions(wordDict)
    example = getExamples(wordDict)
    publishedDate = getpublishedDate(wordDict)
    return render_template("index.html", wordhtml = word, texthtml = text, examplehtml = example, publishedhtml = publishedDate) 

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

if (__name__) == "__main__":
    app.run()