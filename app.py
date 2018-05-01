from flask import *
from page import *
from infoFetch import updatePages

try:
    with open("pages.json", "r") as f:
        pages = eval(f.read())
except FileNotFoundError:
    updatePages()

app = Flask(__name__)

filteredPages = {}

for x in pages:
    if all(pages[x].values()):
        filteredPages[x] = pages[x]

@app.route("/")
def index():
    return render_template("bounty.html")
app.run("0.0.0.0", debug=True)