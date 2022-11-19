#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio
from model import Stock, Order, Match, User
import pymongo

# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://Admin:admin@bloombergdatadb.bhzbby6.mongodb.net/?retryWrites=true&w=majority')

client = pymongo.MongoClient('mongodb+srv://Admin:admin@bloombergdatadb.bhzbby6.mongodb.net/?retryWrites=true&w=majority')

db = client.test

database = client.StockList
collection = database.stock
orderDB = database.orders
userDB = database.users


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
    stocks = []
    cursor = collection.find({})
    for document in cursor:
        stocks.append(Stock(**document))
    return stocks

async def create_stock(stock):
    document = stock
    result = collection.insert_one(document)
    return document

async def fetch_all_stocks_from_one(user):
    stocks = []
    document = user
    cursor = collection.find({"user": user})
    for document in cursor:
        stocks.append(Stock(**document))
    return document
    
async def create_order(order: Order):
    document = order
    result = orderDB.insert_one(document)
    return document

async def fetch_all_orders():
    order = []
    cursor = orderDB.find({})
    for document in cursor:
        order.append(Order(**document))
    return order

async def create_user(user: User):
    document = user
    result = userDB.insert_one(document)
    return document
