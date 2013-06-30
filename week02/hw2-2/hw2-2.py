
import pymongo

connection = pymongo.MongoClient('localhost', 27017)

db = connection.students
collection = db.grades
grades = collection.find({'type': 'homework'}).sort([('student_id', 1), ('score', 1)])

student_id = -1
for g in grades:
    if student_id != g['student_id']:
        student_id = g['student_id']
        print g
        collection.remove({'_id': g['_id']})