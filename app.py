from flask import Flask, render_template
from beeai import *

#Retrive WordDict
wordDict = getwordDict()

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    word = getWord(wordDict)
    
    return render_template("index.html", word=word)

@app.route("/about")
def about_page():
    return render_template("about.html")

if (__name__) == "__main__":
    app.run()