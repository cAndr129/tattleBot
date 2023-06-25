import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://coryandreasen:DRAaVeaLh8Pw3DRc@cluster0.klrv3f4.mongodb.net/?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["tattles"]

#post = {"_id": 0, "name": "tim", "score": 5}
#collection.insert_one(post)

results = collection.find({"name": "bill"})