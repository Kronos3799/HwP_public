from ticket3 import app
from flask import render_template

@app.route('/')
def home_page():
    vars = ["Liki", "Bene", "Joerg"]
    return render_template(template_name_or_list='actors.html', vars=vars)

@app.route('/welcome')
def welcome_page():
    vars = ["Mama", "du hast eine Nachricht"]
    return render_template(template_name_or_list='welcome.html', vars=vars)