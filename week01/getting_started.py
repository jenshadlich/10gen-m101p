
import pymongo

connection = pymongo.MongoClient('localhost', 27017)

db = connection.test
collection = db.names

item = collection.find_one()

print item['name']
