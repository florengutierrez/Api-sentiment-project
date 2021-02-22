from pymongo import MongoClient

client = MongoClient()

db = client.yoda.dialogue

character = db.characters
dialogue = db.text
movie = db.movie

def insert(data):

    res = db.insert_one(data)
    return res.inserted_id


def read(query, project=None):
    data = db.find(query, project)
    return list(data)


def delete(coll, obj):
    removes = coll.remove(obj)
    return remove

def new_character(character,text):
    dic =  {
    "characther":f"{character}",
    "text":f"{text}"
    }
    movie.insert_one(dic)
