from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user")
async  def id_paginator(username: str = 'alex', age: str = '24') -> dict:
    return {"message": f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": 'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def user_id(user_id: Annotated[int, Path(ge=0, le=100, description="Enter your id", example="1")]) -> dict:
    return {"message": f'Вы вошли как пользователь № {user_id}'}

@app.get("/user/{username}/{age}")
async def user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Ivan")], age: int = Path(ge=18, le=120, description="Enter age", example="33")) -> dict:
    return {"message": f'Hello, {username} {age}'}