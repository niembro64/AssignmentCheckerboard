from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def funRoot():
    return 'ROOT'

@app.route('/play/<n>/<c>')
def play(n, c):
    return render_template("index.html", timesN = int(n), phraseColor = c)


if __name__ == "__main__":
    app.run(debug=True)