# app.py
from flask import Flask, jsonify
import perks

app = Flask(__name__) # create an instance of the Flask class


# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    perkIds = perks.perkIds()
    
    response = jsonify({'perks': perkIds})
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# running the server
app.run(debug = True) # to allow for debugging and auto-reload