from ticket import app

HOST = "0.0.0.0"
PORT = 5001
DEBUG = True

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)