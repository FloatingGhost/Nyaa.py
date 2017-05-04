#!/usr/bin/env python3

from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)
database = sqlite3.connect("db.sqlite")

@app.route("/")
def index():
    try:
        pageNo = int(request.args.get("page", 0))
    except:
        pageNo = 0

    cursor = database.cursor()
    ret = cursor.execute("""
        SELECT 
            name
        FROM 
            nyaa
        LIMIT 
            50
        OFFSET 
            (?)
    """, [pageNo * 50])
    return render_template("index.html", rows=list(ret))

if __name__ == "__main__":
    app.run()
