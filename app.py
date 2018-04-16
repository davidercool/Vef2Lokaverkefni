from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome, please donate"

app.run("0.0.0.0", debug=True)