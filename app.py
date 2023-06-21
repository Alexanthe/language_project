from flask import Flask, render_template, request
from markupsafe import Markup
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
    path = request.path
    return render_template("contact.html", currentpath = path)

@app.route("/hive",methods=["GET", "POST"])
def hive_page():
    path = request.path
    if request.method=="POST":

        # getting input from html
        numOfWords = request.form.get("numofwords")
        # getting input from html        
        style = request.form.get("style")

        # getting word from api
        wordDict = getwordDict()
        word = getWord(wordDict)

        prompt = generate_prompt(word, numOfWords, style)
        hiveText = generateHive(prompt)

        data = Markup(hiveText.replace(word, "<mark>"+word+"</mark>"))
        
        return render_template("hive.html", currentpath = path, hive = data, prompt = prompt)
    return render_template("hive.html", currentpath = path)

if (__name__) == "__main__":
    app.run()