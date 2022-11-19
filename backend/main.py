#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

from fastapi import FastAPI, HTTPException

from model import Todo, Stock

from database import (
    fetch_one_stock,
    fetch_all_stocks,
    create_stock,
    update_stock,
    remove_stock,
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
"""
@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")

"""
# For Stocks project here

@app.get("/api/stock")
async def get_stock():
    response = await fetch_all_stocks()
    return response

@app.get("/api/stock/{name}", response_model=Stock)
async def get_stock_by_name(name):
    response = await fetch_one_stock(name)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {id}")

@app.post("/api/stock/", response_model=Stock)
async def post_stock(stock: Stock):
    response = await create_stock(stock.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/stock/{user}/", response_model=Stock)
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
