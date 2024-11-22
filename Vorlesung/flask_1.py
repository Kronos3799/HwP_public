from flask import Flask

app = Flask(__name__) # Klasse Flask erwaretet Dateinamen / Modulnamen als Parameter, daher muss die aufgerufene Datei eingebunden werden (passiert hier durch: __name__)

@app.route("/")
def home_page():
    return "hello_page"

@app.route("/home")
def hello_world():
    return "<h1>Hello, World!</h1><p>It's a beautiful day!</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)