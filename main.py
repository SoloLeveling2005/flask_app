import random

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get/', methods=['GET'])
def index():
    rand = random.randint(1, 1001)
    return f"<h1>{rand}</h1>"

@app.route('/post/', methods=['POST'])
def index():
    rand = random.randint(1, 1001)
    return f"<h1>{rand}</h1>"
# Запуск:
# set FLASK_APP=main
# flask run

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
