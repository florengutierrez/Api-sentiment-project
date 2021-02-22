from flask import Flask, request
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


@app.route("/text_movies/<movie>")
def check_text_movies():
    query = {"movie":movie}
    if not check_params(query,"movie",["1", "3", "6"]):
        return {"Please, select 1, 3 or 6 movie."}
    query2 = read(q, project={"movie":1, "character":1, "text":1, "_id":0})
    return json_util.dumps(query2)



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
