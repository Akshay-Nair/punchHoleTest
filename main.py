from flask import Flask, request
import os
app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def get_my_ip():
    return "hello world"

@app.route("/", methods=["GET"])
def homepage():
    return "<html><body>Hello world</body></html>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

