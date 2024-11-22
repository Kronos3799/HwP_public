from HorseBuy import app

HOST = "0.0.0.0"
PORT = 5002
DEBUG = True

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)

# Bei Mac benötigte Einstellung zur Ausführung im lokalen Netzwerk:

# - Einstellungen -> Netzwerk

#                 -> Firewall ausschalten
#                 -> VPN & Filter -> Filter und Proxys -> McAfee ausschalten