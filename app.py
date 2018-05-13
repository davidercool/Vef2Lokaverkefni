from flask import *
from Scripts.infoFetch import updatePages
from Scripts.dataHandler import *
from Scripts.user import *
from Scripts.resources import *
from Scripts.submission import *

try:
    with open("UserData/pages.json", "r") as f:
        for x in list(eval(f.read()).values()):
            pages[x["name"]] = Page(x["name"], x["translated"], x["views"])
except FileNotFoundError:
    updatePages()

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="PrinceCharlesIV",
    WTF_CSRF_SECRET_KEY="PrinceCharlesVI",
))

handler = Handler("UserData/data.json", "UserData/subdata.json")
print(handler.get_user("admin"))

filteredPages = list(filter(lambda x: not x.translated, list(pages.values())))


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('home.html', untranslatedArticles=filteredPages, enumerate=enumerate, str=str, len=len)


@app.route("/translate", methods=["GET", "POST"])
def editor():
    userID = decrypt(request.cookies.get("userID"))
    if userID is None:
        # ef user er ekki logged in
        return redirect("/login")
    try:
        if handler.get_user(userID) is None:
            # ef user er logged it en ekki til
            return redirect("/login")
        if request.method == "POST":
            text = request.form.get("Text1")
            handler.add_submission(userID, Submission(text, Page("!?unkownPage?!", None, -1), handler.get_user(userID)))
            # ef user er logged in, til og var að submitta
            return "Thanks for the sub"
        # ef user er logged in og til
        return render_template('translation.html')
    except ValueError:
        return "error"


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
                resp = make_response(redirect("/"))
                resp.set_cookie("userID", encrypt(name), max_age=2678400) #31*24*60*60 = 2678400
                return resp
        return render_template("login.html", message="Login failed! Username or password is incorrect.", colors=["#FF5343", "#7F2A22"])
    else:
        return render_template("login.html", message=None)


@app.route("/search")
def search():
    s = request.args.get('s')
    l = request.args.get('l')
    o = request.args.get('o')
    if s == None:
        return render_template("search.html", results=None)
    l = 20 if l is None else l
    o = 0 if o is None else o
    try:
        return str(get_searches(s,l,o))
    except:
        return "Unknown error"


@app.route("/logout")
def logout():
    resp = make_response(redirect("/"))
    resp.delete_cookie("userID")
    return resp


app.run("0.0.0.0", debug=True)