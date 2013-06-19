
import pymongo

connection = pymongo.MongoClient('localhost', 27017)

db = connection.names
collection = db.names

for item in collection.find():
    print item
