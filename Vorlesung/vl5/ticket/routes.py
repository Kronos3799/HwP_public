from ticket import app, db
from flask import Response, render_template, request, url_for, redirect, flash
from sqlalchemy import text

@app.route('/')
def home_page():
    cookie = request.cookies.get('name')
    print("<>home_page", cookie)
    return render_template('home.html', cookie=cookie)

@app.route('/tickets')
def tickets_page():
    cookie = request.cookies.get('name')
    print("<>tickets_page", cookie)
    if not request.cookies.get('name'):
        return redirect(url_for('login_page'))
    query_stmt = f"select * from testitems"
    result = db.session.execute(text(query_stmt))
    itemsquery = result.fetchall()

    return render_template('tickets.html', items=itemsquery)

@app.route('/login', methods=['GET','POST'])
def login_page():
    print(">>>>>>login_page")
    if request.method == 'POST':
        username = request.form.get('username')
        email_address = request.form.get('email_address')
        password = request.form.get('password')

        if username is None or isinstance(username, str) is False:
            print("something wrong with username")
            return render_template('login.html', cookie=None)
        if email_address is None or isinstance(email_address, str) is False:
            print("something wrong with email_address")
            return render_template('login.html', cookie=None)
        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("something wrong with password")
            return render_template('login.html', cookie=None)

        query_stmt = f"SELECT username FROM testusers WHERE username='{username}' and email_address='{email_address}' and password='{password}'"
        print(query_stmt)
        result = db.session.execute(text(query_stmt))
        user = result.fetchall()

        if not user:
            print("try again ....")
            #flash(f"Try again", category='warning')
            return render_template('login.html')

        print("testing redirect")
        resp=redirect('/tickets')
        resp.set_cookie('name', username)
        return resp

    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register_page():
    print(">>>>>>register_page")
    if request.method == 'POST':
        username = request.form.get('username')
        email_address = request.form.get('email_address')
        password = request.form.get('password')

        if username is None or isinstance(username, str) is False:
            print("something wrong with username")
            return render_template('register.html')
        if email_address is None or isinstance(email_address, str) is False:
            print("something wrong with email_address")
            return render_template('register.html')
        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("something wrong with password")
            return render_template('register.html')

        query_stmt = f"INSERT INTO testusers (username, email_address, password) VALUES ('{username}', '{email_address}', '{password}');"
        print(query_stmt)
        db.session.execute(text(query_stmt))
        db.session.commit()
        return redirect(url_for('login_page'))

    return render_template('register.html')

@app.route('/logout')
def logout_page():
    Response.delete_cookie('name')
    return redirect(url_for('home_page'))