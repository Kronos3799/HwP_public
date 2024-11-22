from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("actors.html")

@app.route("/welcome")
def welcome():
    vars = {}
    vars["username"] = "John"
    vars["message"] = "Welcome to the site!"
    return render_template("welcome.html", vars=vars)

@app.route("/quest")
def quest():
    name = request.args.get("name", "John")
    return render_template("quest.html", var=name)

if __name__ == "__main__":
    app.run(debug=True) # Defaultwerte werden genutzt, wenn keine Parameter angegeben werden