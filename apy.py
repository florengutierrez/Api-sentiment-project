from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util
from helpers.mongoConnection import *
from helpers.checking import check_params, check_exists
from bson import ObjectId
from add import *

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

@app.route("/movie/new")
def  movie_new():
    args = dict(request.args)
    id = add_movie(args)
    return json_util.dumps({"_id":id})


if __name__ == "__main__":
    app.run(debug=True)
