from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    return "hello_page"


@app.route("/home")
def hello_world():
    return "<h1>Hello W0rld</h1><p>this is home</p>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)

