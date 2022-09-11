import os
from flask import Flask, jsonify
import rook

app = Flask(__name__)
rook.start(labels={"env": "dev"}, token='09243394571cc46f395ba2cdd7805b47b54c0b707847392067f8878b17fc5012')


@app.route("/")
def handler():
    return jsonify({
        'item': 'aaa',
        'amount': 1
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
