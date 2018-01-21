from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)


@app.route('/info')
def main():
    return render_template("index.html")

@app.route('/')
def welcome():
    return render_template("welcome.html")

if __name__ == '__main__':
    app.run()
