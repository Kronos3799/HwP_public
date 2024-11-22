from HorseBuy import app, db
from flask import render_template, request, redirect, url_for, jsonify, make_response
from sqlalchemy import text


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        address = request.form.get('address')

        if username is None or isinstance(username, str) is False:
            print("Something went wrong - username")
            return render_template("register.html")
        
        if firstname is None or isinstance(firstname, str) is False:
            print("Something went wrong - firstname")
            return render_template("register.html")
        
        if lastname is None or isinstance(lastname, str) is False:
            print("Something went wrong - lastname")
            return render_template("register.html")
        
        if email is None or isinstance(email, str) is False:
            print("Something went wrong - email")
            return render_template("register.html")
        
        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("Something went wrong - password")
            return render_template("register.html")
        
        if address is None or isinstance(address, str) is False:
            print("Something went wrong - address")
            return render_template("register.html")
        
        query_stmt = f"insert into user (username, firstname, lastname, email, password, address) values ('{username}', '{firstname}', '{lastname}', '{email}', '{password}', '{address}')"
        db.session.execute(text(query_stmt))
        db.session.commit()

        return redirect(url_for('login_page'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username is None or isinstance(username, str) is False:
            print("Something went wrong - username")
            return render_template('login.html', cookie=None)
        
        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("Something went wrong - password")
            return render_template('login.html', cookie=None)
        
        query_stmt = f"select username from user where username = '{username}' and password = '{password}'"
        result = db.session.execute(text(query_stmt))
        user = result.fetchone()

        if not user:
            print("User not found")
            return render_template("login.html")
        
        resp=redirect('/shop')
        resp.set_cookie('name', username)
        return resp
    
    return render_template("login.html")


@app.route('/shop', methods=['GET', 'POST'])
def shop_page():
    cookie = request.cookies.get('name')
    if not request.cookies.get('name'):
        return redirect(url_for('login_page'))
    
    query_stmt = f"select * from item"
    result = db.session.execute(text(query_stmt))
    itemsquery = result.fetchall()

    return render_template("shop.html", items=itemsquery, cookie=cookie)

@app.route('/member', methods=['GET', 'POST'])
def member_page():
    cookie = request.cookies.get('name')
    if not request.cookies.get('name'):
        return redirect(url_for('login_page'))

    searchedMember = request.args.get('searchedMember')

    if searchedMember is None or isinstance(searchedMember, str) is False:
        query_stmt = f"select username, firstname, lastname, email from user"
        result = db.session.execute(text(query_stmt))
        userquery = result.fetchall()

    else:
        query_stmt = f"select username, firstname, lastname, email from user where username = '{searchedMember}'"
        # SQL Injection mit folgendem Statement möglich - Leerzeichen am Ende beachten:
        #' union select username, password, lastname, email from user -- 
        result = db.session.execute(text(query_stmt))
        userquery = result.fetchall()
    
    return render_template("member.html", user=userquery, cookie=cookie)


@app.route('/account', methods=['GET', 'POST'])
def user_page():
    cookie = request.cookies.get('name')
    if not request.cookies.get('name'):
        return redirect(url_for('login_page'))
    
    query_stmt = f"select * from user where username = '{cookie}'"
    result = db.session.execute(text(query_stmt))
    userquery = result.fetchall()

    return render_template("account.html", user=userquery, cookie=cookie)


@app.route('/userProducts', methods=['GET', 'POST'])
def userProducts_page():
    cookie = request.cookies.get('name')
    if not request.cookies.get('name'):
        return redirect(url_for('login_page'))
    
    # User ID aus Cookie extrahieren
    query_stmt_user_ID = f"select id from user where username = '{cookie}'"
    result = db.session.execute(text(query_stmt_user_ID))
    user_ID = result.fetchall()[0][0]
    
    query_stmt = f"select * from item where user = '{user_ID}'"
    result = db.session.execute(text(query_stmt))
    itemsquery = result.fetchall()

    return render_template("userProducts.html", items=itemsquery, cookie=cookie)


@app.route('/changeUser', methods=['GET', 'POST'])
def changeUser_page():
    cookie = request.cookies.get('name')
    if not request.cookies.get('name'):
        return redirect(url_for('login_page'))
    
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        address = request.form.get('address')

        if firstname is None or isinstance(firstname, str) is False:
            print("Something went wrong - firstname")
            return render_template("changeUser.html")
        
        if lastname is None or isinstance(lastname, str) is False:
            print("Something went wrong - lastname")
            return render_template("changeUser.html")
        
        if email is None or isinstance(email, str) is False:
            print("Something went wrong - email")
            return render_template("changeUser.html")
        
        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("Something went wrong - password")
            return render_template("changeUser.html")
        
        if address is None or isinstance(address, str) is False:
            print("Something went wrong - address")
            return render_template("changeUser.html")
        
        query_stmt = f"update user set firstname = '{firstname}', lastname = '{lastname}', email = '{email}', password = '{password}', address = '{address}' where username = '{cookie}'"
        db.session.execute(text(query_stmt))
        db.session.commit()

        return redirect(url_for('user_page'))
    
    return render_template("changeUser.html", cookie=cookie)


@app.route('/addProduct', methods=['GET', 'POST'])
def addProduct_page():
    cookie = request.cookies.get('name')
    if not request.cookies.get('name'):
        return redirect(url_for('login_page'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        info = request.form.get('info')

        price = float(price) # vorher Datentyp str

        if name is None or isinstance(name, str) is False:
            print("Something went wrong - name")
            return render_template("addProduct.html")
        
        if price is None or isinstance(price, float) is False:
            print("Something went wrong - price")
            return render_template("addProduct.html")
        
        if info is None or isinstance(info, str) is False:
            print("Something went wrong - info")
            return render_template("addProduct.html")
        
        # User ID aus Cookie extrahieren
        query_stmt_user_ID = f"select id from user where username = '{cookie}'"
        result = db.session.execute(text(query_stmt_user_ID))
        user_ID = result.fetchall()[0][0]

        query_stmt = f"insert into item (name, price, info, user) values ('{name}', {price}, '{info}', '{user_ID}')"
        db.session.execute(text(query_stmt))
        db.session.commit()

        return redirect(url_for('userProducts_page'))
    
    return render_template("addProduct.html", cookie=cookie)

@app.route('/deleteProduct', methods=['DELETE'])
def deleteProduct_page():
    productID = request.args.get('id')

    if productID is None:
        return jsonify({"error": "Invalid productID."}), 400
        
    query_stmt = f"delete from item where id = {productID}"
    db.session.execute(text(query_stmt))
    db.session.commit()

    return jsonify({"message": "Product deleted successfully."}), 200


@app.route('/logout')
def logout():
    response = redirect(url_for('login_page'))
    response.delete_cookie('name')
    return response


@app.route('/deleteAccount', methods=['DELETE'])
def delete_account():
    cookie = request.cookies.get('name')
    if not request.cookies.get('name'):
        return redirect(url_for('login_page'))
    
    if not cookie:
        return "Invalid account.", 400
        
    query_stmt = f"delete from user where username = '{cookie}'"
    db.session.execute(text(query_stmt))
    db.session.commit()    

    resp = make_response("Account deleted successfully.", 200)
    resp.delete_cookie('name')
    return resp  