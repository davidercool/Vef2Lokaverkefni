from flask import *
from page import *
from infoFetch import updatePages

try:
    with open("pages.json", "r") as f:
        pages = eval(f.read())
except FileNotFoundError:
    updatePages()

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome, please donate"

app.run("0.0.0.0", debug=True)