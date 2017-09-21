#! /usr/bin/env python
# -*-encoding:utf-8-*-
# __author:physics
# app.py

import sqlite3, time
from flask import Flask, request, render_template, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)


def get_db():
    db = sqlite3.connect('mydb.db')
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    rv = cur.fetchall()
    db.close()
    return (rv[0] if rv else None) if one else rv

def get_gs8():
    db = TinyDB('gs8.json')
    q = Query()
    lst = []
    for i in [str(a)[1:] for a in range(101,113,1)]:
        item = db.search(q.create_time.search('2017-{}-*'.format(i)))
        if len(item) > 0:
            lst.append(['{}月'.format(int(i)),len(item)])
        else:
            lst.append(['{}月'.format(int(i)), 0])
    db.close()
    print(lst)
    return lst
# get_gs8()
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST","GET"])
def weather():
    if request.method == "POST":
        res = query_db("SELECT * FROM weather")

    return jsonify(month=[x[0] for x in res],
                   evaporation=[x[1] for x in res],
                   precipitation=[x[2] for x in res])

# result = get_gs8()
@app.route("/gs8",methods=['POST','GET'])
def gs8():
    if request.method == 'POST':
        t1 = time.time()
        res = get_gs8()
        print('it cost {} s!'.format(time.time()-t1))
    return jsonify(month=[x[0] for x in res],
                   nums = [x[1] for x in res])



if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1',port=8080)