import os
from flask import Flask, jsonify, request
import rook
import requests
app = Flask(__name__)
rook.start()

ORDERS_SRV_URL = "https://orders-service-g7jhom5g6q-uc.a.run.app"


@app.route("/")
def default_handler():
    return jsonify(data={"status": "ok"})


@app.route("/order", methods=["POST"])
def order_post():
    resp = requests.post(url=f'{ORDERS_SRV_URL}/order', json={
        'item_id': request.json['item_id'],
        'amount': request.json['amount'],
        'shipping_address': request.json['shipping_address']
    }).json()

    if "error" in resp:
        return jsonify({
            "error": resp["error"]
        })

    return jsonify({
        "total": resp['total'],
        "tracking_number": resp['tracking_num'],
    })


if __name__ == "__main__":
    ORDERS_SRV_URL = "http://127.0.0.1:8082"
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
