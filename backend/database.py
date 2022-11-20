#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

# import motor.motor_asyncio
from model import Stock, Order, User
import pymongo
# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://Admin:admin@bloombergdatadb.bhzbby6.mongodb.net/?retryWrites=true&w=majority')

client = pymongo.MongoClient('mongodb+srv://Admin:admin@bloombergdatadb.bhzbby6.mongodb.net/?retryWrites=true&w=majority')

db = client.test

database = client.StockList
collection = database.stock
orderDB = database.orders
userDB = database.users
matchingDB = database.match


# users



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

async def create_user(user: User):
    document = user
    result = userDB.insert_one(document)
    return document

async def fetch_all_stocks_from_one(user: str):
    stocks = []
    cursor = collection.find({"user": user})
    for doc in cursor:
        stocks.append(Stock(**doc))
    return stocks
    
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
"""
async def create_matching(match: Match):
    document = match
    result = matchingDB.insert_one(document)
    return document
"""

async def get_last_user(username: str):
    return userDB.find({"username": username})

async def fetch_all_orders_from_one(customer: str):
    orders = []
    cursor = orderDB.find( {"customer": customer})
    for doc in cursor:
        orders.append(Order(**doc))
    return orders

async def match(name: str, side: str, qty: str, price: str, customer: str):
    
    order = []
    cursor = orderDB.find({})
    for document in cursor:
        order.append(Order(**document))
    print(name, side, qty, price, customer)
    temp_data = []
    
    for i in range(0, len(order)):
        if ((order[i].name) == (name)) and ((order[i].customer) != (customer)) and ((order[i].side) != (side)):
            # same stock, buyer and seller and differnet side
            temp_data.append(order[i])
    print(temp_data)
    maxquant = 0
    max_i = 0
    while (int(qty) > 0) and (len(temp_data) != 0):
        
        for i  in range(0, len(temp_data)):
            if int(temp_data[i].qty) >= maxquant:
                maxquant = int(temp_data[i].qty)
                max_i = i

        if int(qty) >= int(temp_data[max_i].qty):
            tmp = int(temp_data[max_i].qty)
            orderDB.delete_one({"name": temp_data[max_i].name, "side": temp_data[max_i].side, "qty": temp_data[max_i].qty, "price": temp_data[max_i].price, "customer": temp_data[max_i].customer})
            
            if side == "SELL":
                await push_stock_to_user(name, qty, customer, temp_data[max_i].customer)
            else:
                await push_stock_to_user(name, tmp, temp_data[max_i].customer, customer)
            
            del temp_data[max_i]
            qty = int(qty) - tmp
        else:
            tmp = int(temp_data[max_i].qty) - int(qty)
            filter = {"name": temp_data[max_i].name, "side": temp_data[max_i].side, "qty": temp_data[max_i].qty, "price": temp_data[max_i].price, "customer": temp_data[max_i].customer}
            update = {"$set": {"qty": tmp}}
            stock = orderDB.find_one_and_update(filter, update)
            qty = "0"
            
    if qty == "0":
        orderDB.delete_one({"name": name, "side": side, "qty": qty, "price": price, "customer": customer})

async def push_stock_to_user(name:str, qty: str, user: str, user2: str):
    print(name, qty, user, user2)
    filter = {"name": name, "user":user}
    update = {"$set": {"qty": qty, "user":user2}}
    stock = collection.find_one_and_update(filter, update)
    
