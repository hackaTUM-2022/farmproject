#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

from fastapi import FastAPI, HTTPException

from model import Stock, Order, Match, User

from database import (
    fetch_one_stock,
    fetch_all_stocks,
    create_stock,
    update_stock,
    remove_stock,
    fetch_all_stocks_from_one,
    create_order,
    fetch_all_orders,
    create_user
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

@app.get("/api/stock")
async def get_stock():
    response = await fetch_all_stocks()
    return response

@app.get("/api/order")
async def get_all_orders():
    response  = await fetch_all_orders()
    return response

@app.get("/api/stock/{name}", response_model=Stock)
async def get_stock_by_name(name):
    response = await fetch_one_stock(name)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {id}")

@app.get("/api/stock/{user}", response_model=Stock)
async def get_all_stocks_from_user(user):
    response = await fetch_all_stocks_from_one(user)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {user}")

@app.post("/api/stock", response_model=Stock)
async def post_stock(stock: Stock):
    response = await create_stock(stock.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/stock/{user}", response_model=Stock)
async def put_user(user: str):
    response = await update_stock(user)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {user}")

@app.delete("/api/stock/{user}")
async def delete_user(user):
    response = await remove_stock(user)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {user}")


@app.post("/api/order", response_model=Order)
async def post_order(order: Order):
    response = await create_order(order.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.post("api/login", response_model=User)
async def register_user(user: User):
    response = await create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")
