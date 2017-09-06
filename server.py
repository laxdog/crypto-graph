from flask import Flask, render_template
import sqlite3
import json

app = Flask(__name__)


def json_min(results):
    return json.dumps(results, separators=(',', ':'))


def run_query(query, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


@app.route("/polo.json")
@app.route("/crypto-graph/polo.json")
def polo():
    db = "polo.db"
    query = "SELECT unixtime, round(rate0 * 100, 5) FROM loans WHERE unixtime % 10 = 0 ORDER BY unixtime ASC;"
    results = run_query(query, db)
    return json_min(results)


@app.route("/finex.json")
@app.route("/crypto-graph/finex.json")
def finex():
    db = "finex.db"
    query = "SELECT unixtime, round(rate0 * 100, 5) FROM loans WHERE unixtime % 2 = 0 ORDER BY unixtime ASC;"
    results = run_query(query, db)
    return json_min(results)


@app.route("/eth-polo.json")
@app.route("/crypto-graph/eth-polo.json")
def eth_polo():
    db = "ETH-polo.db"
    query = "SELECT unixtime, round(rate0 * 100, 5) FROM loans WHERE unixtime % 60 = 0 ORDER BY unixtime ASC;"
    results = run_query(query, db)
    return json_min(results)


@app.route("/eth-finex.json")
@app.route("/crypto-graph/eth-finex.json")
def eth_finex():
    db = "ETH-finex.db"
    query = "SELECT unixtime, round(rate0 * 100, 5) FROM loans WHERE unixtime % 60 = 0 ORDER BY unixtime ASC;"
    results = run_query(query, db)
    return json_min(results)


@app.route("/btc-polo.json")
@app.route("/crypto-graph/btc-polo.json")
def btc_polo():
    db = "BTC-polo.db"
    query = "SELECT unixtime, round(rate0 * 100, 5) FROM loans WHERE unixtime % 60 = 0 ORDER BY unixtime ASC;"
    results = run_query(query, db)
    return json_min(results)


@app.route("/btc-finex.json")
@app.route("/crypto-graph/btc-finex.json")
def btc_finex():
    db = "BTC-finex.db"
    query = "SELECT unixtime, round(rate0 * 100, 5) FROM loans WHERE unixtime % 60 = 0 ORDER BY unixtime ASC;"
    results = run_query(query, db)
    return json_min(results)


@app.route("/")
def graph():
    return render_template('graph.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='127.0.0.1', port=3044)
