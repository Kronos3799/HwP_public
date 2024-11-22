from hackingnews import app, db
from flask import render_template, request, url_for, redirect, make_response, flash
from sqlalchemy import text
from markdown import markdown
from datetime import date

# ---------- get user cookie ----------
def user_id_cookie():
    return request.cookies.get('user')

def user_name_cookie():
    user_id=user_id_cookie()
    if user_id:
        query = f"SELECT username FROM user WHERE id={user_id};"
        result = db.session.execute(text(query))
        row = result.fetchone()
        return row[0]
    return None

# ---------- get current date ----------
def get_current_date():
    return date.today().isoformat()

# ---------- index page ----------
@app.route('/')
def home_page():
    print(">>>>>home_page")

    login = False
    if user_id_cookie():
        login = True

    query = "SELECT id, title, LEFT(content, 1000) FROM article;"
    result = db.session.execute(text(query))
    table = result.fetchall()
    articles = []
    for row in table:
        articles.append({'id': row[0], 'title': row[1], 'content': markdown(row[2])})
    
    return render_template('index.html', login=login, articles=articles)

# ---------- article page ----------
@app.route('/article')
def article_page():
    print(">>>>>article_page")

    login = False
    if user_id_cookie():
        login = True

    article_id = int(request.args.get('id', type=int))
    query = f"SELECT a.title, u.username, a.publication_date, a.content, premium FROM article AS a JOIN user AS u ON u.id=a.author WHERE a.id={article_id};"
    result = db.session.execute(text(query))
    row = result.fetchone()
    article = {'title': row[0], 'author': row[1], 'publication_date': row[2], 'content': markdown(row[3])}
    premium = row[4]

    print(f"premium: {premium}, login: {login}")
    if premium and not login:
        flash("This article is premium. Please login to read the full article.", "error")
        return redirect(url_for('home_page'))

    return render_template('article.html', login=login, article=article)

# ---------- article editor page ----------
@app.route('/article-editor')
def article_editor_page():
    print(">>>>>article_editor_page")
    
    if not user_id_cookie():
        return redirect(url_for('login_page'))
    login = True

    query = "SELECT id, title FROM article;"
    result = db.session.execute(text(query))
    table = result.fetchall()
    articles = []
    for row in table:
        articles.append({'id': row[0], 'title': row[1]})
    
    return render_template('article-editor.html', login=login, articles=articles)

@app.route("/article-editor", methods=['POST'])
def article_editor_post():
    print(">>>>>article_editor_post")

    user_cookie = user_id_cookie()
    if not user_cookie:
        return redirect(url_for('login_page'))

    id = request.form.get('id')
    title = request.form.get('title')
    content = request.form.get('content')
    premium = request.form.get('premium')
    print(f"id: {id}, title: {title}, date: {get_current_date()}, content: {content}, premium: {premium}")
    if premium == "on":
        premium = 1
    else:
        premium = 0

    # check if title and content are strings and not empty
    if title is None or isinstance(title, str) is False or len(title) == 0:
        flash("title is missing", "error")
        return redirect(url_for('article_editor_page'))
    if content is None or isinstance(content, str) is False or len(content) == 0:
        flash("content is missing", "error")
        return redirect(url_for('article_editor_page'))

    # check if id is a number
    if id is not None and id.isdigit() is False:
        # if id is not a number, create a new article
        query = text(f"INSERT INTO article (title, author, publication_date, content, premium) VALUES ('{title}', {user_cookie}, '{get_current_date()}', :content, {premium});")
    else:
        # if id is a number, update the article
        query = text(f"UPDATE article SET title='{title}', author={user_cookie}, publication_date='{get_current_date()}', content=:content, premium={premium} WHERE id={id};")
    
    if db.session.execute(query, {'content': content}):
        db.session.commit()
    else:
        flash("database error", "error")
        return redirect(url_for('article_editor_page'))

    return redirect(url_for('home_page'))

@app.route('/article-editor/get', methods=['GET'])
def article_editor_get():
    print(">>>>>article_editor_get")

    if not user_id_cookie():
        return redirect(url_for('login_page'))

    article_id = request.args.get('id')
    print(f"article_id: {article_id}")
    if article_id is None:
        flash("id is missing", "error")
        return "id is missing", 400
    elif article_id == "new":
        article = {'title': '', 'content': '', 'id': 'new'}
        return article, 200
    else:
        query = f"SELECT title, content, premium FROM article WHERE id={article_id};"
        result = db.session.execute(text(query))
        row = result.fetchone()
        article = {'title': row[0], 'content': row[1], 'premium': row[2]}
        return article, 200

@app.route('/article-editor/delete', methods=['DELETE'])
def article_editor_delete():
    print(">>>>>article_editor_delete")

    if not user_id_cookie():
        return redirect(url_for('login_page'))

    article_id = request.args.get('id')
    print(f"article_id: {article_id}")
    if article_id is None:
        flash("id is missing", "error")
        return "id is missing", 400
    elif article_id == "new":
        return "OK", 200
    else:
        query = f"DELETE FROM article WHERE id={article_id};"
        if db.session.execute(text(query)):
            db.session.commit()
        else:
            flash("database error", "error")
            return "database error", 500
        flash("article deleted", "success")
        return "OK", 200

# ---------- authors page ----------
@app.route('/authors', methods=['GET', 'POST'])
def authors_page():
    print(">>>>>authors_page")

    login = False
    if user_id_cookie():
        login = True

    query = "SELECT username, email FROM user;"

    if request.method == 'POST':
        search = request.form.get('search')
        if search is not None:
            query = f"SELECT username, email FROM user WHERE username LIKE '%{search}%';"
        
    print(query)
    result = db.session.execute(text(query))
    table = result.fetchall()
    authors = []
    for row in table:
        author = []
        for col in row:
            author.append(col)
        authors.append(author)

    return render_template('authors.html', login=login, authors=authors)

# ---------- account page ----------
@app.route('/account')
def account_page():
    print(">>>>>account_page")
    
    user_cookie = user_name_cookie()
    if not user_cookie:
        return redirect(url_for('login_page'))
    login = True

    query = f"SELECT username, email FROM user WHERE username='{user_cookie}';"
    result = db.session.execute(text(query))
    row = result.fetchone()
    user = {'username': row[0], 'email': row[1]}
    
    return render_template('account.html', login=login, user=user)

@app.route('/account', methods=['POST'])
def account_post():
    print(">>>>>account_post")

    user_cookie = user_id_cookie()
    if not user_cookie:
        return redirect(url_for('login_page'))
    
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    new_password = request.form.get('new_password')

    if username is None or isinstance(username, str) is False:
        flash("username is missing", "error")
        return redirect(url_for('account_page'))
    if email is None or isinstance(email, str) is False:
        flash("email is missing", "error")
        return redirect(url_for('account_page'))
    if password is None or isinstance(password, str) is False:
        flash("password is missing", "error")
        return redirect(url_for('account_page'))
    
    # check if password is correct
    query = f"SELECT id FROM user WHERE id={user_cookie} and password='{password}';"
    result = db.session.execute(text(query))
    row = result.fetchone()
    if not row:
        print("password is wrong")
        flash("password is wrong", "error")
        return redirect(url_for('account_page'))
    
    # update user data
    if new_password is None or isinstance(new_password, str) is False:
        query = f"UPDATE user SET username='{username}', email='{email}' WHERE id={user_cookie};"
    else:
        if len(new_password) < 3:
            flash("new password is too short", "error")
            return redirect(url_for('account_page'))
        query = f"UPDATE user SET username='{username}', email='{email}', password='{new_password}' WHERE id={user_cookie};"
    
    db.session.execute(text(query))
    db.session.commit()

    flash("user data updated", "success")
    return redirect(url_for('account_page'))

@app.route('/account/delete', methods=['POST'])
def account_delete():
    print(">>>>>account_delete")

    user_cookie = user_id_cookie()
    if not user_cookie:
        return redirect(url_for('login_page'))

    password = request.form.get('password')
    if password is None or isinstance(password, str) is False:
        flash("password is missing", "error")
        return "password is missing", 400
    query = f"SELECT id FROM user WHERE id={user_cookie} and password='{password}';"
    result = db.session.execute(text(query))
    row = result.fetchone()
    if not row:
        flash("password is wrong", "error")
        return "password is wrong", 400

    query = f"DELETE FROM user WHERE id={user_cookie};"
    db.session.execute(text(query))
    db.session.commit()

    
    flash("user deleted", "success")
    resp = make_response("OK", 200)
    resp.delete_cookie('user')
    return resp

# ---------- login page ----------
@app.route('/login' , methods=['GET','POST'])
def login_page():
    print(">>>>>login_page")
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"username: {username}, password: {password}")

        if username is None or isinstance(username, str) is False:
            flash("username is missing", "error")
            return render_template('login.html')
        if password is None or isinstance(password, str) is False or len(password) < 3:
            flash("password is missing", "error")
            return render_template('login.html')

        query = f"SELECT id FROM user WHERE username='{username}' and password='{password}';"
        print(query)
        result = db.session.execute(text(query))
        row = result.fetchone()
        
        if not row:
            flash("username or password is wrong", "error")
            return render_template('login.html')
        else:
            user_id = str(row[0])
            resp=redirect("/")
            resp.set_cookie("user", user_id)

            return resp
    
    return render_template('login.html')

# ---------- register page ----------
@app.route('/register', methods=['GET','POST'])
def register_page():
    print(">>>>>register_page")
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        print(f"username: {username}, email: {email}, password: {password}")

        if username is None or isinstance(username, str) is False:
            flash("username is missing")
            return render_template('register.html')
        if email is None or isinstance(email, str) is False:
            flash("email is missing", "error")
            return render_template('register.html')
        if password is None or isinstance(password, str) is False or len(password) < 3:
            flash("password is missing", "error")
            return render_template('register.html')

        query = f"INSERT INTO user (username, email, password) VALUES ('{username}', '{email}', '{password}');"
        print(query)
        db.session.execute(text(query))
        db.session.commit()

        query = f"SELECT id FROM user WHERE username='{username}';"
        result = db.session.execute(text(query))
        row = result.fetchone()
        user_id = str(row[0])

        resp=redirect("/")
        resp.set_cookie("user", user_id)
        return resp
    
    return render_template('register.html')

# ---------- logout page ----------
@app.route('/logout')
def logout_page():
    print(">>>>>logout_route")

    response = redirect(url_for('home_page'))
    response.delete_cookie('user')
    
    return response