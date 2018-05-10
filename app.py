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

filteredPages = list(filter(lambda x: not x.translated, list(pages.values())))


@app.route("/")
def index():
    return render_template('bounty.html', untranslatedArticles=filteredPages, enumerate=enumerate, str=str, len=len)


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