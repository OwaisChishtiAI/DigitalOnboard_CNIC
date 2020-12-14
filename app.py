from cnic_reality import check_reality
from flask import Flask, Response, jsonify, request

app = Flask(__name__)


@app.route('/v2/detect_cnic', methods=["POST"])
def detect_cnic():
    frame = request.form["image"]

    temp = check_reality(frame)

    if (temp):
        return "", 200

    return "", 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
