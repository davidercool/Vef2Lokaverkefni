from flask import *
from page import *
from infoFetch import updatePages

try:
    with open("pages.json", "r") as f:
        for x in list(eval(f.read()).values()):
            pages[x["name"]] = Page(x["name"], x["translated"], x["views"])
except FileNotFoundError:
    updatePages()

app = Flask(__name__)

filteredPages = list(filter(lambda x: not x.translated, list(pages.values())))

@app.route("/")
def index():
    return render_template('bounty.html', untranslatedArticles = filteredPages, enumerate=enumerate, str=str, len=len)
app.run("0.0.0.0", debug=True)