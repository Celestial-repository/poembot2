# app.py

from flask import Flask, render_template, redirect, url_for, jsonify
import poembot2

app = Flask(__name__)

@app.route('/')
def hello():
    return "I'm sorry Dave.  I cannot do that."

@app.route('/poem')
def poem():
    poem = poembot2.generate_poem()
    return render_template('poem.html', poem=poem)


if __name__ == '__main__':
    app.run(debug=True)