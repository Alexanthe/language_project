from flask import Flask, render_template
from beeai import *

#Retrive WordDict
wordDict = getwordDict()

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    word = getWord(wordDict)
    source, text  = getDefinitions(wordDict)
    example = getExamples(wordDict) # Create a function that can Extract text and title from dictionary in bee.py or have check jinja if can extract???
    return render_template("index.html", wordhtml = word, texthtml = text)

@app.route("/about")
def about_page():
    return render_template("about.html")

if (__name__) == "__main__":
    app.run()