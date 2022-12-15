import pymongo
from pymongo import MongoClient


cluster = pymongo.MongoClient("mongodb+srv://hans:rupwTH9cVbCgGZht@nodecluster.gknsvxa.mongodb.net/?retryWrites=true&w=majority")
db = cluster["basketball_data"]
collection = db["stats"]

print("test")