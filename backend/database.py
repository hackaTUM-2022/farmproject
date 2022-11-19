#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio
from model import Todo, Stock
import pymongo

# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://Admin:admin@bloombergdatadb.bhzbby6.mongodb.net/?retryWrites=true&w=majority')

client = pymongo.MongoClient('mongodb+srv://Admin:admin@bloombergdatadb.bhzbby6.mongodb.net/?retryWrites=true&w=majority')

db = client.test

database = client.StockList
collection = database.stock
""""
db = client.test

database = client.TodoList
collection = database.todo

async def fetch_one_todo(title):
    document = collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = collection.insert_one(document)
    return document
    
async def update_todo(title, desc):
    collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = collection.find_one({"title": title})
    return document

async def remove_todo(title):
    collection.delete_one({"title": title})
    return True
"""

async def update_stock(user):
    collection.update_one({"user": user})
    document = collection.find_one({"user": user})
    return document

async def remove_stock(user):
    collection.delete_one({"user": user})
    return True

async def fetch_one_stock(title):
    document = collection.find_one({"title": title})
    return document

async def fetch_all_stocks():
    todos = []
    cursor = collection.find({})
    for document in cursor:
        todos.append(Stock(**document))
    return todos

async def create_stock(stock):
    document = stock
    result = collection.insert_one(document)
    return document
