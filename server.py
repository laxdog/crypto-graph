from flask import Flask, render_template
import sqlite3
import json

app = Flask(__name__)


@app.route("/polo.json")
def polo():
    connection = sqlite3.connect("{0}/MACD_testing/market_data/BTC.db".format(os.environ['HOME']))
    cursor = connection.cursor()
    cursor.execute("SELECT unixtime * 1000, rate0 * 100 FROM loans ORDER BY unixtime ASC;")
    results = cursor.fetchall()
    return json.dumps(results)


@app.route("/finex.json")
def finex():
    connection = sqlite3.connect("{0}/macd_bitfinex/market_data/BTC.db".format(os.environ['HOME']))
    cursor = connection.cursor()
    cursor.execute("SELECT unixtime * 1000, rate0 * 100 FROM loans ORDER BY unixtime ASC;")
    results = cursor.fetchall()
    return json.dumps(results)


@app.route("/")
def graph():
    return render_template('graph.html')


if __name__ == '__main__':
    app.run(debug=False, threaded=True, host='127.0.0.1', port=3044)
