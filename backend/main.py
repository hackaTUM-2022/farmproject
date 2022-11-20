#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

from fastapi import FastAPI, HTTPException

from model import Stock, Order, User

from database import (
    fetch_one_stock,
    fetch_all_stocks,
    create_stock,
    update_stock,
    remove_stock,
    fetch_all_stocks_from_one,
    create_order,
    fetch_all_orders,
    create_user,
    get_last_user,
    fetch_all_orders_from_one,
    match
    
)

# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "*",
]

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# For Stocks project here

#STOCKS

@app.get("/api/stock")
async def get_stock():
    response = await fetch_all_stocks()
    return response

@app.get("/api/stock/name/{name}", response_model=Stock)
async def get_stock_by_name(name):
    response = await fetch_one_stock(name)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {id}")

@app.get("/api/stock/{user}")
async def get_all_stocks_from_user(user):
    response = await fetch_all_stocks_from_one(user)
    return response
    
@app.post("/api/stock", response_model=Stock)
async def post_stock(stock: Stock):
    response = await create_stock(stock.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/stock/update/{user}", response_model=Stock)
async def put_user(user: str):
    response = await update_stock(user)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {user}")

@app.delete("/api/stock/delete/{user}")
async def delete_user(user):
    response = await remove_stock(user)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {user}")


# ORDER
@app.get("/api/order")
async def get_all_orders():
    response  = await fetch_all_orders()
    return response

@app.post("/api/order", response_model=Order)
async def post_order(order: Order):
    response = await create_order(order.dict())
    if response:
        await match(order.name, order.side, order.qty, order.price, order.customer)
        return response
    raise HTTPException(400, "Something went wrong")

@app.get("/api/order/{customer}")
async def get_all_orders_from_user(customer):
    response = await fetch_all_orders_from_one(customer)
    return response

# LOGIN
@app.post("/api/login", response_model=User)
async def register_user(user: User):
    response = await create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.get("/api/lastuser")
async def give_last_user(user: str):
    return await get_last_user(user)
    

# MATCH
"""
@app.post("/api/match", response_model=Match)
async def post_matching(match: Match):
    response = await create_matching(match.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")
"""

"""@app.get("/api/match/{name}/{side}/{qty}/{price}/{customer}")
async def matching(name: str, side: str, qty: str, price: str, customer: str):
    return await match(name, side, qty, price, customer)"""
