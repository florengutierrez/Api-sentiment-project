from helpers.checking import *
from helpers.mongoConnection import *
from bson import ObjectId

def add_movie(obj):
    if not check_params(obj,["movie", "character", "text"]):
        return {"please add movie, character and text"}
    query = {"movie":obj["movie"]}

    if check_exists(q,"movie"):
        return {"hey! the episodes 1, 3 and 6 already exists"}
    res = write_coll("movie",obj)
    return res.inserted_id
