from ticket import app
from flask import render_template

@app.route("/")
def home_page():
    vars = ["Kylo", "Luke", "Nat"]
    return render_template(template_name_or_list="actors.html", vars=vars)

@app.route("/welcome")
def welcome():
    vars = ["Kylo", "you are on dark side"]
    return render_template(template_name_or_list="welcome.html", vars=vars)