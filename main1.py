from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

class item(BaseModel):
    id:int
    name:str
    description:str
    price:int

@app.put("/api/v1/{itemid}")
def add_item(itemid:int,item:item):
    return {"id":item.id,"name":item.name,"description":item.description,"price":item.price}

@app.post("/api/v1/{itemid}")
def add_item(itemid:int,item:item):
    return {"id":itemid,"name":item.name,"description":item.description,"price":item.price}

@app.get("/greet")
def get_optional(name:Optional[str]="shobha"):
    return {"message" : f"hello {name}"}

            
   
    

    