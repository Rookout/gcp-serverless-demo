import os
from flask import Flask, jsonify, request
import rook
import requests

app = Flask(__name__)
rook.start(labels={"env": "dev"})

INVENTORY_SRV_URL = "https://inventory-service-g7jhom5g6q-uc.a.run.app"
SHIPPING_SRV_URL = "https://shipping-service-g7jhom5g6q-uc.a.run.app"


@app.route("/order", methods=["POST"])
def order():
    order_req = request.json

    inventory_resp = requests.post(f'{INVENTORY_SRV_URL}/update', json={
        "item_id": order_req['item_id'],
        "action": "reserve",
        "amount": order_req['amount']
    }).json()

    if "error" in inventory_resp:
        return jsonify({"error": inventory_resp['err']})

    shipping_resp = requests.post(f'{SHIPPING_SRV_URL}/shipment', json={
        "item_id": order_req['item_id'],
        "address": order_req['shipping_address']
    }).json()

    if "error" in shipping_resp:
        return jsonify({"error": shipping_resp['error']})

    return jsonify({
        "total": inventory_resp['total'],
        "tracking_num": shipping_resp['tracking_num']
    })


if __name__ == "__main__":
    INVENTORY_SRV_URL = "http://127.0.0.1:8081"
    SHIPPING_SRV_URL = "http://127.0.0.1:8083"
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8082)))
