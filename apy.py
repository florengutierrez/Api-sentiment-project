from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util
from helpers.mongoConnection import *
from helpers.checking import check_params, check_exists
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost/yoda"
mongo = PyMongo(app)

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

"""@app.route("/movie/<movie>")
def movie(movie):
    query = {"movie":movie}
    if not check_exists(query,"movie",["1", "3", "6"]):
        return {"Please, select 1, 3 or 6."}
    query2 = read(query = read({"character":"YODA"}, project={"character":1, "text":1, "_id":0})

    return json_util.dumps(query2)"""


if __name__ == "__main__":
    app.run(debug=True)
