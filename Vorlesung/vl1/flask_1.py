from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "hello page"

@app.route("/home")
def hello_world():
    return "<h1>Hello World</h1><p>this is home</p>"

if __name__ == "__main__":
    print("website running...")
    app.run(debug=True, host="0.0.0.0", port=8888)