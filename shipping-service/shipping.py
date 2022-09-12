import os
from flask import Flask, jsonify, request
import rook

app = Flask(__name__)
rook.start(labels={"env": "dev"})


@app.route("/")
def handler():
    return jsonify({'status': 'ok'})


@app.route("/shipment", methods=["POST"])
def update():
    shipment_req = request.json
    if shipment_req['address'] == "/dev/null":
        return jsonify({
            'error': "bad address supplied",
        })

    return jsonify({
        'item_id': shipment_req['item_id'],
        'status': 'shipped',
        'tracking_num': '123-abc'
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8083)))
