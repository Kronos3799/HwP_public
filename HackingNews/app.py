from hackingnews import app

EXTERN = True
HOST = '0.0.0.0'
PORT = 5001
DEBUG = True

if __name__ == "__main__":
    if EXTERN:
        app.run(host=HOST, port=PORT, debug=DEBUG)

    else:
        app.run(host='127.0.0.1', port=PORT, debug=True)