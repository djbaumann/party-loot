from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route("/")
def main():
    return "welcome!"


if __name__ == "__main__":
    app.run()
