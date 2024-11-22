from ticket import app
from flask import render_template

@app.route("/")
def home_page():
    vars = ["Kylo", "Luke", "Nat"]
    return render_template("home.html")

@app.route("/tickets")
def tickets_page():
    items = [{"id": 1, "priority": 2, "username": "Mark", "title": "nothing works"},
             {"id": 2, "priority": 1, "username": "John", "title": "everything messed up"},
             {"id": 3, "priority": 3, "username": "Luke", "title": "I am lost"}
            ]
    return render_template("tickets.html", items=items)