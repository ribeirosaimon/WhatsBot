from flask import Flask, request, jsonify
from create_json_api import *


app = Flask(__name__)

@app.route("/")
def all_stocks():
    for x in principal_stocks:
        try:
            json_stock = find_stock(x)
        except Exception as e:
            pass

if __name__ == "__main__":
    app.run(debug=True)
