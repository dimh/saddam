import sys
from flask import Flask, render_template, session
app = Flask(__name__, static_url_path = "", static_folder = "templates/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=['GET', 'POST'])
def play():
    return render_template("juego.html", word='_H_O_L_A')

@app.route("/lose", methods=['GET'])
def lose():
    return render_template("lose.html")

@app.route("/win", methods=['GET'])
def win():
    return render_template("win.html")

if __name__ == '__main__':
    app.run()