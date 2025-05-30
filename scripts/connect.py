from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client.test
print("Connexion MongoDB réussie :", db)
