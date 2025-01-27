from fastapi import FastAPI

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
async def user(user_id: str) -> dict:
    return {"message": f'Вы вошли как пользователь № {user_id}'}