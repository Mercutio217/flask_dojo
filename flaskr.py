from flask import Flask, request, render_template, url_for, redirect
import os
import sqlite3

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "flask_dojo.db")

app = Flask(__name__)
@app.route("/")
def main():
    return "Check this out!"

@app.route("/counter", methods=["GET", "POST"])
def counter():
    base = sqlite3.connect("flask_dojo.db")
    cursor = base.cursor()
    if request.method == "GET":
        cursor.execute("UPDATE counter SET get_counter = get_counter + 1")
        base.commit()
    elif request.method == "POST":
        cursor.execute("UPDATE counter SET post_counter = post_counter + 1")
        base.commit()
    base.close()
    return "DB UPDATED!"

@app.route("/statistics")
def statistics():
    base = sqlite3.connect("flask_dojo.db")
    base_tuple = base.execute("SELECT * FROM counter")
    for item in base_tuple:
        get_counter = item[0]
        post_counter = item[1]

    return "Get counter: {} Post counter: {}".format(get_counter, post_counter)

@app.route("/statistics")
def return_to_root():
    main()

if __name__ == "__main__":
    app.run()