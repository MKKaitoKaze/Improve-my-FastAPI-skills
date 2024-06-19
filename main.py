from fastapi import FastAPI
from datebase import users
from datebase import fake_trades
from typing import List
from pydantic import Field
from operator import ge
from datebase import Trade
from datebase import User


app = FastAPI(
    title = "First program   on FastAPI"
)

@app.get("/users/{users_id}", response_model=List[User])
def get_users_id(user_id: int):
    return [user for user in users if user.get("id") == user_id]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}

@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}