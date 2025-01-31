from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_all_users() -> List[User]:
    return users

@app.post(path="/user/{username}/{age}")
async def add_user(user: User) -> str:
    user.id = len(users)
    users.append(user)
    return f"User id {user.id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return f"The user {user_id} is updated"
    except:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User id {user_id} was deleted"
    except:
        raise HTTPException(status_code=404, detail="User not found")
