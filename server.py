from flask import Flask, render_template
import functools
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


def generic_get(db, query):
    results = run_query(query, db)
    return json_min(results)

routes = {}
currencies = ["BTC", "ETH", "XMR", "LTC", "DOGE", "MAID", "BTS", "STR", "CLAM", "FCT", "DASH", "XRP", "BCH", "DSH",
              "ETC", "IOT", "OMG", "ZEC", "EOS", "USD"]
exchanges = ["POLONIEX", "BITFINEX"]
#query = "SELECT unixtime, round(rate0 * 100, 5) FROM loans WHERE unixtime % 60 = 0 ORDER BY unixtime ASC;"
query = "SELECT unixtime, round(rate0 * 100, 3) FROM loans WHERE unixtime ORDER BY unixtime ASC;"
for cur in currencies:
    for ex in exchanges:
        name = "{0}-{1}".format(ex, cur)
        routes[name] = functools.partial(generic_get, "{0}.db".format(name), query)
        app.add_url_rule('/{0}'.format(name), name, routes[name])
        app.add_url_rule('/crypto-graph/{0}'.format(name), name, routes[name])

@app.route("/")
def graph():
    return render_template('graph.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='127.0.0.1', port=3044)
