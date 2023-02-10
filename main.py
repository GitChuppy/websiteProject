from flask import Flask, request, send_from_directory, jsonify
from passlib.hash import argon2 as A2
from database_functions import registerUser, getUserData
import uuid


app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("static/account", "login.html") #TODO Send to home-/landing-page

@app.route("/login")
def login():
    return send_from_directory("static/account", "login.html") #TODO Send to home-/landing-page

@app.route("/register")
def register():
    return send_from_directory("static/account", "register.html") #TODO Send to home-/landing-page

@app.route("/api/login", methods=["POST"])
def login_api():

    loginData = { #TODO optimize hashing and salting using Argon2. 3 Iterations of hashing according to german wikipedia with "64MiB" of RAM usage(?)
                    'username'      :   request.form['usernameLogin'], #TODO change email to a username, so that we can also hash that!
                    'password'      :   request.form['passwordLogin'] #TODO use .verify(string, hash) for login!
                }

    try:
        if A2.verify(loginData['password'], getUserData(usernameLogin=loginData['username'], type='password')):
            return jsonify({
                "message": "logIn",
                "address": "/userpage" #FIXME userpage
                })
    except:
        
        # for returning loginErrors:
        return jsonify({"message"   :   "userLoginError"})

    return jsonify({"message"   :   "userLoginError"})

@app.route("/api/register", methods=["POST"])
def register_api():
    #TODO check if user is registered already...
    registerData = { #TODO optimize hashing and salting using Argon2. 3 Iterations of hashing according to german wikipedia with "64MiB" of RAM usage(?)
                    'uuidRegister'      :                               str(uuid.uuid4())                   ,
                    'usernameRegister'  :                               request.form['usernameRegister']    ,
                    'emailRegister'     :                               request.form['emailRegister']       ,   #TODO change email to a username, so that we can also hash that!
                    'passwordRegister'  :   A2.using(rounds=3).hash(    request.form['passwordRegister'])       #TODO use verify(string, hash) for login!
                }
    try:
        registerUser(dict= registerData)
        return "1302: REGISTERED" #TODO Send to userpage
    except:
        return "1299: USERNAME OR EMAIL ALREADY TAKEN" #TODO Send GET/POST to user, informing that either of both has been taken

if __name__ == "__main__":
    app.run(debug=True)#, host="192.168.1.105", port=80)
    #TODO REMOVE DEBUG MODE FOR SHIPPING, AND DEPLOY WITH A SSL CERT ONTO WSGI
