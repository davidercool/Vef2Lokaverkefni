import urllib.request
from flask import *
from page import *
from infoFetch import updatePages
from dataHandler import Handler
from user import *

try:
    with open("pages.json", "r") as f:
        for x in list(eval(f.read()).values()):
            pages[x["name"]] = Page(x["name"], x["translated"], x["views"])
except FileNotFoundError:
    updatePages()

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="PrinceCharlesIV",
    WTF_CSRF_SECRET_KEY="PrinceCharlesVI"
))

handler = Handler("UserData/data.json")
print(handler.evaluated())
print(handler.get_user("bob"))

filteredPages = list(filter(lambda x: not x.translated, list(pages.values())))


@app.route("/")
def index():
    return render_template('home.html', untranslatedArticles=filteredPages, enumerate=enumerate, str=str, len=len)

@app.route("/translate")
def editor():
    return render_template('translation.html')

@app.route("/bounty")
def bounty():
    return render_template('bounty.html', untranslatedArticles=filteredPages, enumerate=enumerate, str=str, len=len)

@app.route("/u/<username>")
def userpage(username):
    if handler.get_user(username) is not None:
        return render_template('userpage.html', user=handler.get_user(username))

    return "404"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        mail = request.form.get("email")
        passw = request.form.get("passw")
        if handler.add_user(User(name, mail, passw)):
            return render_template("login.html", message="Signup was successful! Now please log in.", colors=["#40FF40", "#207F20"])
        return render_template("signup.html", message="Signup Failed! Username already in use.", colors=["#FF5343", "#7F2A22"])
    else:
        return render_template("signup.html", message=None)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        passw = request.form.get("passw")
        user = handler.get_user(name)
        if user is not None:
            if decrypt(user.passw) == passw:
                return redirect("/")
        return render_template("login.html", message="Login failed! Username or password is incorrect.", colors=["#FF5343", "#7F2A22"])
    else:
        return render_template("login.html", message=None)

app.run("0.0.0.0", debug=True)