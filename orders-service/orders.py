import os
from flask import Flask, jsonify
import rook
import requests

app = Flask(__name__)
rook.start(labels={"env": "dev"}, token='09243394571cc46f395ba2cdd7805b47b54c0b707847392067f8878b17fc5012')

INVENTORY_SRV_URL = "https://inventory-service-g7jhom5g6q-uc.a.run.app"
SHIPPING_SRV_URL = "https://shipping-service-g7jhom5g6q-uc.a.run.app"


@app.route("/")
def handler():
    resp = requests.get(f'{INVENTORY_SRV_URL}/?item=1')
    resp = requests.get(f'{SHIPPING_SRV_URL}/?item=1')
    return jsonify(resp.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
