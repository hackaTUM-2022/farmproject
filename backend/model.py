from pydantic import BaseModel
from decimal import *

class Todo(BaseModel):
    title: str
    description: str

class Stock(BaseModel):
    name: str
    qty: str
    price: str
    user: str
    
class Order(BaseModel):
    name: str
    side: str
    qty: str
    price: str
    customer: str
    
"""
class Match(BaseModel):
    buyer: str
    seller: str
    stockname: str
    buyerStockId: str
    sellerStockId: str
    qty: str
    price: str
"""
class User(BaseModel):
    username: str
    password: str
    
