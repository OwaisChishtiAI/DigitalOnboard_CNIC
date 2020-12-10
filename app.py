from flask import Flask, Response, jsonify, request
from cnic_reality import CheckReality

app = Flask(__name__)


@app.route('/v2/detectcnic', methods=["POST"])
def detectCNIC():
    frame = request.form["image"]

    temp = CheckReality(frame)

    if (temp):
        return "", 200

    return "", 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
