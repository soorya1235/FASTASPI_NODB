from fastapi import FastAPI,HTTPException
from typing import List
from models import User
from uuid import uuid4,UUID
from models import User,Gender
from models import Role,userupdaterequest

app = FastAPI()

db : List[User] = [
    User(
    id = UUID("e6519597-262a-41c5-a00c-d22a95dbd605"),
    first_name="soorya",
    last_name ="saravanan",
    gender=Gender.male,
    roles=[Role.student]
    ),
     User(
    id = UUID("e6519597-262a-41c5-a00c-d22a95dbd605"),
    first_name="choti",
    last_name ="lakshmi",
    gender=Gender.female,
    roles=[Role.student,Role.admin]
    )
]


@app.get("/")
async def root():
    return {"hello" : "soorya"}


@app.get("/api/v1/user")
async def root():
    return db

@app.get("/api/v1/user/{customer}")
async def root(customer:int):
    return {"message" : f"customer is {customer}"}

"""
Here in the above API if we pass string like below "http://127.0.0.1:8000/api/v1/user/soorya"
we get pydantic validation errorl
"detail": [
{
"loc": [
"path",
"customer"
],
"msg": "value is not a valid integer",
"type": "type_error.integer"
}
]
}
"""
@app.post("/api/v1/users")
async def create(user : User):
    db.append(user)
    return user.id

@app.delete("/api/v1/users/{userid}")
async def delete_user(userid : UUID):
    for user in db:
        if user.id == userid:
            db.remove(user)
            return
    raise HTTPException(status_code=404,detail=f"user with {user.id} does not exists")    

@app.put("/api/v1/users/{userid}")
async def update_user(user_update : userupdaterequest,userid : UUID):
    for user in db:
        if user.id == userid:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return        
    raise HTTPException(status_code=404,detail=f"user with {user.id} does not exists")            
                


