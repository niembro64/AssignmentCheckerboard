from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def funRoot():
    return 'ROOT CHECKERBOARD'

@app.route('/<col>/<row>/<color1>/<color2>')
def play(col, row, color1, color2):
    return render_template("index.html", Rcol = int(col), Rrow = int(row), Rcolor1 = color1, Rcolor2 = color2)


if __name__ == "__main__":
    app.run(debug=True)