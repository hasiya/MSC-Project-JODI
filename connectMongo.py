from pymongo import MongoClient


def connect_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.datasets

    return db


# def insert

def createCollection(collectionName, datasetObject):
    db = connect_db()
    collection = db[collectionName]

    db[collectionName].insert_one(datasetObject)

# createCollection("test2", {'a': 1})
