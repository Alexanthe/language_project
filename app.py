# set FLASK_APP = app.py
# $env:FLASK_ENV = "development"  # ON debug mode
# flask run

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/about")
def about():
    return "About this project.."
