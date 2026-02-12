from pymongo import MongoClient
from os import getenv

MONGODB_COLLECTION = getenv('MONGODB_COLLECTION')
MONGO_URI = getenv('MONGO_URI')
MONGODB_DATABASE = getenv('MONGODB_DATABASE')


class MongoDB:
    def __init__(self):
        self.client = MongoClient(
            host=MONGO_URI,
            port=27017
            )

    def get_collection(self):
        db = self.client[MONGODB_DATABASE]
        collection = db[MONGODB_COLLECTION]
        return collection

    def get_n_records(self, n: int, skip: int = 0):
        collection = self.get_collection()
        result = collection.find({}).skip(skip).limit(n)
        return result


