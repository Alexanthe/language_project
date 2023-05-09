from flask import Flask, render_template
from beeai import *



app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    #Retrive WordDict
    wordDict = getwordDict()
    word = getWord(wordDict)
    source, text  = getDefinitions(wordDict) #put source beside definition
    example = getExamples(wordDict) #put title beside text. 
    return render_template("index.html", wordhtml = word, texthtml = text, examplehtml = example) 

@app.route("/about")
def about_page():
    return render_template("about.html")

if (__name__) == "__main__":
    app.run()