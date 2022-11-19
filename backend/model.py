#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

# Pydantic allows auto creation of JSON Schemas from models
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
    
class Match(BaseModel):
    buyer: str
    seller: str
    name: str
    qty: str
    price: str
    
class User(BaseModel):
    username: str
    password: str
