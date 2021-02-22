from pymongo import MongoClient

client = MongoClient()

db = client.yoda.dialogue

characters = client.yoda.characters
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

#creo una nueva colección en MongoDB de character para facilitar el proceso.
def get_personages():
    query = {}
    project = {"character":1, "_id":0}
    char = (list(characters.find(query, project)))
    return char