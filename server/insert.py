import pymongo
import json

myclient = pymongo.MongoClient("mongodb://user:pass1234@localhost:27017/")
mydb = myclient["halodoc"]
mycol = mydb["medicine"]

with open("data.json", "r") as f:
    mylist = json.load(f)

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)

# # define the column you want to delete
# column_to_delete = 'apotek'

# # loop through every document in the collection and delete the column
# for doc in mycol.find():
#     if column_to_delete in doc:
#         del doc[column_to_delete]
#         mycol.replace_one({'_id': doc['_id']}, doc)
