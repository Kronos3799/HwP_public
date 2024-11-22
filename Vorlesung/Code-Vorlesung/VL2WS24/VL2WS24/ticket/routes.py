from ticket import app
from flask import render_template

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/tickets')
def tickets_page():
    items = [{"id":1, "priority": 2, "username": "Mark", "title": "nothing works"},
             {"id":2, "priority": 1, "username": "Derk", "title": "all is broken"},
             {"id":3, "priority": 3, "username": "Natalie", "title": "not looking good"}
             ]

    return render_template("tickets.html", items=items)

