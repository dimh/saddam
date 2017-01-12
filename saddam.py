import sys
from flask import Flask, render_template, session
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=['GET', 'POST'])
def play():
    return render_template("juego.html", word='_H_O_L_A')

if __name__ == '__main__':
    app.run()