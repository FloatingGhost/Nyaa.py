#!/usr/bin/env python3

from flask import Flask, render_template, redirect, request
import sqlite3
import json

app = Flask(__name__)
database = sqlite3.connect("db.sqlite")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query")
def query():
    cursor = database.cursor()
    print(request.form)
    return json.dumps({
        "draw":request.args.get("draw"),
        "recordsTotal":1,
        "recordsFiltered":1,
        "data": [
                    {"name":"a"}
                ],
    })
if __name__ == "__main__":
    app.run()
