from flask import Flask, request, send_from_directory
from passlib.hash import argon2 as A2
import uuid

import sys
from os.path import dirname
sys.path.append(dirname(__file__))

import dbHandlerMOD as dbHandler

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("static/login", "login.html") #TODO Send to home-/landing-page

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        loginData = { #TODO optimize hashing and salting using Argon2. 3 Iterations of hashing according to german wikipedia with "64MiB" of RAM usage(?)
                        'username'      :   request.form['usernameLogin'], #TODO change email to a username, so that we can also hash that!
                        'password'      :   A2.using(rounds=3).hash(request.form['passwordLogin']) #TODO use .verify(string, hash) for login!
                    }
        print(loginData)
    return "1301: LOGGED-IN" #TODO Send to userpage

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        #TODO check if user is registered already...
        registerData = { #TODO optimize hashing and salting using Argon2. 3 Iterations of hashing according to german wikipedia with "64MiB" of RAM usage(?)
                        'uuidRegister'      :                               str(uuid.uuid4())                   ,
                        'usernameRegister'  :                               request.form['usernameRegister']    ,
                        'emailRegister'     :                               request.form['emailRegister']       ,   #TODO change email to a username, so that we can also hash that!
                        'passwordRegister'  :   A2.using(rounds=3).hash(    request.form['passwordRegister'])       #TODO use verify(string, hash) for login!
                    }
        
        dbHandler.registerUser(dict= registerData, tuple= dbHandler.startSession())
        return "1302 REGISTERED" #TODO Send to userpage

if __name__ == "__main__":
    app.run(debug=True)
    #TODO REMOVE DEBUG MODE FOR SHIPPING