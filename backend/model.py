#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

# Pydantic allows auto creation of JSON Schemas from models
from pydantic import BaseModel
from decimal import *

class Todo(BaseModel):
    title: str
    description: str

class Stock(BaseModel):
    typ: str
    name: str
    side: str
    qty: Decimal
    price: Decimal
    user: str
