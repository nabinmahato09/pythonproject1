from pymongo import MongoClient


client = MongoClient("mongodb+srv://youtubepy:<db_password>@cluster0.g8bu2ln.mongodb.net/")
#  Not a good idea to include id and password in code files

db = client["ytmanager"]
