import os
from flask import Flask, jsonify, request
import rook

app = Flask(__name__)
rook.start()


@app.route("/")
def handler():
    return jsonify({'status': 'ok'})


@app.route("/update", methods=["POST"])
def update():
    update_req = request.json

    return jsonify({
        'item_id': update_req['item_id'],
        'total': 100 * update_req['amount']
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8081)))
