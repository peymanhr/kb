from pymongo import MongoClient
from pprint import pprint

#client = MongoClient('mongodb://192.168.1.41:27017/')

client = MongoClient('mongodb://192.168.1.41:27017/',
                    username='admin', password='ost')

db = client["people"]
collection = db['friends']

# mydict = { "name": "John", "address": "Highway 37" }
# result = collection.insert_one(mydict)
# print(result.inserted_id)

# dblist = client.list_database_names()
# print(dblist)

# friends = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
#
# result = collection.insert_many(friends)
# print(result.inserted_ids)

# doc = collection.find_one()
# print(doc)

# for doc in collection.find():
#   print(type(doc), doc)

# for doc in collection.find({},{ '_id': 0, 'name': 1, 'address': 1 }):
#   print(doc)


# # query = { 'address': 'Park Lane 38' }
# # query = { 'address': { '$gt': 'S' } }
# # query = { "address": { "$regex": "^S" } }
# docs = collection.find(query)
# for doc in docs:
#   print(doc)

# # query = { "address": { "$regex": "^S" } }
# # docs = collection.find(query).sort('name')
# docs = collection.find(query).sort('name', -1)
# for doc in docs:
#   print(doc)

# result = collection.delete_one(query)
# result = collection.delete_many(query)
# result = collection.delete_many({}) # Truncate

# collection.drop()

# $inc
# query = { 'name': 'Viola' }
# newvalues = { '$set': { 'address': 'Tehran' } }
# # result = collection.update_one(query, newvalues)
# # result = collection.update_many(query, newvalues)
# for d in collection.find():
#   print(d)
# # print(result.modified_count)
# # print(help(result))
# # print(result.raw_result)

# docs = collection.find().limit(5)
# for doc in docs:
#   print(doc)
