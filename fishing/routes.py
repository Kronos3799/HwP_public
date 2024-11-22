import os
from fishing import app, bcrypt, ALLOWED_EXTENSIONS, db
from flask import render_template, request, redirect, url_for, jsonify, make_response
from werkzeug.utils import secure_filename
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, set_access_cookies, unset_jwt_cookies
from sqlalchemy import text, exc
    

@app.route('/home', methods=["GET", "POST"])
def home_page():
    if not request.cookies.get('access_token_cookie'):
        return redirect(url_for('login_page'))
    if request.method == 'POST':
        username = request.form['filter']
        sqlStmt = f'SELECT *, DATE_FORMAT(added, "%d.%m.%Y") FROM fishs where username like "%{username}%"'
    else:
        sqlStmt = 'SELECT *, DATE_FORMAT(added, "%d.%m.%Y") FROM fishs'
    result = db.session.execute(text(sqlStmt))
    fishList = result.fetchall()
    return render_template('home.html', homeVisible=True, loggedOut=False, fishList=fishList)

@app.route('/')
def login_page():
    return render_template('login.html', homeVisible=False, loggedOut=True)

@app.route('/register')
def register_page():
    return render_template('register.html', homeVisible=False, loggedOut=True)

@app.route('/profile')
@jwt_required()
def profile_page():
    username = get_jwt_identity()
    queryStmt = f'SELECT *, DATE_FORMAT(added, "%d.%m.%Y") from fishs WHERE username = "{username}"'
    result = db.session.execute(text(queryStmt))
    fishList = result.fetchall()
    return render_template('profile.html', fishList=fishList, homeVisible=True, loggedOut=False, username=username)

@app.route('/showFish/<id>')
@jwt_required()
def showFish_page(id):
    username = get_jwt_identity()
    queryStmt = f'SELECT *, DATE_FORMAT(added, "%d.%m.%Y") from fishs WHERE id = "{id}"'
    result = db.session.execute(text(queryStmt))
    fish = result.fetchone()
    return render_template('showFish.html', fish=fish, homeVisible=True, loggedOut=False, username=username)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/loginUser", methods=["GET", "POST"])
def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 1' or '1' = '1
        # SELECT * FROM USERS WHERE username = '1' or '1' = '1' and password = '1' or '1' = '1'
        #sqlStmt = f"SELECT * from users WHERE username = '{username}' and password = '{password}'"
        sqlStmt = f"SELECT * from users WHERE username = '{username}'"
        result = db.session.execute(text(sqlStmt))
        user = result.fetchone()
    
        if user is None:
            return jsonify({"msg": "Bad username or password"}), 401
        if not bcrypt.check_password_hash(user[1], password):
            return jsonify({"msg": "Bad username or password"}), 401

        resp = redirect(url_for('home_page'))
        access_token = create_access_token(identity=username)
        resp.set_cookie("access_token_cookie", value=access_token)
        #set_access_cookies(resp, access_token)
        return resp

@app.route('/signout')
def sign_out():
    resp = redirect(url_for('login_page'))
    resp.set_cookie('access_token_cookie', '', expires=0)
    return resp

@app.route('/registerUser', methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        
        hashedPassword = bcrypt.generate_password_hash(password.encode('utf-8'))
        hashedPassword = hashedPassword.decode('ascii')
        sqlStmt = f"INSERT INTO users (username, password) VALUES ('{username}', '{hashedPassword}')"
        try:
            db.session.execute(text(sqlStmt))
            db.session.commit()
        except exc.SQLAlchemyError as err:
            print(err)
    return redirect(url_for('login_page'))

        
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/addNewFish', methods=['GET', 'POST'])
def add_new_fish():
    if request.method == 'POST':
        username = request.form['username']
        fish = request.form['fish']
        size = request.form['size']
        weight = request.form['weight']
        filename="noImage.png"
        if 'image' in request.files:
            file = request.files['image']
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            sqlStmt = f"INSERT INTO fishs (fish, size, weight, picture, username) VALUES ('{fish}', {size}, {weight}, '{filename}', '{username}')"
            db.session.execute(text(sqlStmt))
            db.session.commit()

    return redirect(url_for('profile_page'))

@app.route("/fish/<id>", methods=["DELETE"])
def fish_delete(id):
    if request.method == 'DELETE':
        sqlStmt = f'DELETE from fishs where id = {id}'
        db.session.execute(text(sqlStmt))
        db.session.commit()
        return jsonify({"msg": "Fish deleted successfully"}), 200

@app.route("/editFish/<id>")
@jwt_required()
def edit_fish(id):
    username = get_jwt_identity()
    # SELECT * from fishs where id = '3' OR 1=1 AND username = "..."
    sqlStmt = f'SELECT * from fishs where id = {id} AND username = "{username}"'
    print(sqlStmt)
    result = db.session.execute(text(sqlStmt))
    fish = result.fetchone()
    if fish is None:
        return jsonify({"msg": "Fish doesn't exist or user is not the owner"}), 404
    return render_template('editFish.html', homeVisible=True, loggedOut=False, fish=fish)

@app.route("/updateFish/", methods=["POST"])
def update_fish():
    if request.method == "POST":
        id = request.form["id"]
        fish = request.form['fish']
        size = request.form['size']
        weight = request.form['weight']
        if 'picture' in request.files:
            file = request.files['picture']
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                sqlStmt = f'UPDATE fishs SET fish = "{fish}", size = "{size}", weight = "{weight}", picture = "{filename}" where id = {id}'
            if file.filename == "":
                sqlStmt = f'UPDATE fishs SET fish = "{fish}", size = "{size}", weight = "{weight}" where id = {id}'    
        db.session.execute(text(sqlStmt))
        db.session.commit()
    return redirect(url_for('profile_page'))

