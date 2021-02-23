from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from helpers.mongoConnection import *
from helpers.checking import check_params, check_exists
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost/yoda"
mongo = PyMongo(app)


##ENDPOINTS

@app.route('/')
def Yodapi():
    return "Welcome to Yodapi" 

@app.route("/salute")
def salute():
   
    return  "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering."

@app.route("/yoda")
def phrases():
    query = read({"character":"YODA"}, project={"character":1, "text":1, "_id":0})
    return json_util.dumps(query)

@app.route("/characters")
def list_characters():
    chars = get_personages()
    return jsonify(chars)

# Estas dos me han dejado de tirar, buscando el arreglo.

"""@app.route("/new_character", methods=["POST"])
def insert_new_character():
    character = request.form.get("character")
    dialogue = request.form.get("text")
    new_character(character, dialogue)
    return "text added" """

"""
@app.route("/text-delete")
def text_delete():
    args = dict(request.args)
    return json_util.dumps(delete("texts",args))"""


if __name__ == "__main__":
    app.run(debug=True)
