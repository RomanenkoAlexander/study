from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users_db = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users() -> dict:
    return users_db

@app.post("/user/{username}/{age}")
async def add_user(username, age) -> str:
    current_index = str(int(max(users_db, key=int)) + 1)
    new_user = f"Имя: {username}, возраст: {age}"
    users_db[current_index] = new_user
    return f"User id {current_index} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id, username, age) -> str:
    updated_user = f'Имя: {username}, возраст: {age}'
    users_db[user_id] = updated_user
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id) -> str:
    users_db.pop(user_id)
    return f"User id {user_id} was deleted"
