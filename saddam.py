import sys
from flask import Flask, render_template, session, request
from models.saddam import Saddam
from models.words import Word
app = Flask(__name__, static_url_path = "", static_folder = "templates/static")
word = Word()
saddam = Saddam(word.generar_palabra())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        saddam.buscar(request.form.get('letter_box'))
        score = 10
    else:
        score = 0
    return render_template("juego.html", word=saddam.ofuscada(), score=score)

@app.route("/lose", methods=['GET'])
def lose():
    return render_template("lose.html")

@app.route("/win", methods=['GET'])
def win():
    return render_template("win.html")

if __name__ == '__main__':
    app.run()