from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')


db = client.test_database

testdb = db.dataset

testdb.insert_one({"value": "taco"})



# result = posts.insert_one(post_data)
