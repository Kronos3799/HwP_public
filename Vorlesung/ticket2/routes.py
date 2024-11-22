from ticket3 import app
from flask import render_template

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/tickets')
def welcome_page():
    items = [{"id": 1, "priority": 2, "username": "Bene", "title": "alles kaputt"}]
    # hier eig mehrere Beispeieleinträge

    return render_template(template_name_or_list="tickets.html", items=items)
