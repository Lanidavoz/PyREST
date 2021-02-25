from flask import Flask, jsonify    # Flask constructor and jsonify function

app = Flask(__name__)   # Creating a Flask object and storing in app var

#   Array of dictionaries
accounts = [
    {'name': "Billy", 'balance': 450.00},
    {'name': "Bob", 'balance': 550.00}
]

@app.route("/accounts", methods = ["GET"])    # API endpoint and method

def getAccounts():                          # Function definition in Python
    return jsonify(accounts)

if __name__ == '__main__':  # Call app.run in the main routine
    app.run(port=8080)