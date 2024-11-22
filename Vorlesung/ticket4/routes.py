from ticket4 import app, db
from flask import render_template, request, redirect, url_for
from sqlalchemy import text

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/tickets')
def ticket_page():
    query_stmt = f"select * from testitems"
    result = db.session.execute(text(query_stmt))
    itemsquery = result.fetchall()

    return render_template('tickets.html', items = itemsquery)    

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        email_address = request.form.get('email_address')
        password = request.form.get('password')

        if username is None or isinstance(username, str) is False:
            print("Something went wrong - username")
            return render_template("login.html")
        
        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("Something went wrong - password")
            return render_template("login.html")
        
        query_stmt = f"select username from testusers where username = '{username}' and email_address ='{email_address}' and password = '{password}'"
        print(query_stmt)
        result = db.session.execute(text(query_stmt))
        user = result.fetchall()

        if not user:
            print("User not found")
            return render_template("login.html")
        
        return redirect(url_for('home_page'))
    
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form.get('username')
        email_address = request.form.get('email_address')
        password = request.form.get('password')

        if username is None or isinstance(username, str) is False:
            print("Something went wrong - username")
            return render_template("register.html")
        
        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("Something went wrong - password")
            return render_template("register.html")
        
        query_stmt = f"insert into testusers (username, email_address, password) values ('{username}', '{email_address}', '{password}')"
        db.session.execute(text(query_stmt))
        db.session.commit()

        return redirect(url_for('login_page'))
    
    return render_template("register.html")

