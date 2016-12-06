import requests
from flask import Flask
from flask import render_template
app = Flask(__name__)

api_key = "?"

@app.route("/")
def hello():
    return "Well, hi there friends! Head on over to /search/<album> to search for an album."

@app.route("/search/<album>")
def search(album):
    x=requests.get("http://ws.audioscrobbler.com/2.0/?method=album.search&album=" + album + "&api_key=" + api_key +"&format=json").content
    return x

@app.route("/<name>")
def templ(name):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run()

