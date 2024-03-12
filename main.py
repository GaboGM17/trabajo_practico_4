from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4, UUID


app = FastAPI()

fake_users_db = {
    "1": {"id": "1", "name": "Gabriel", "email": "gabriel@gmail.com"},
    "2": {"id": "2", "name": "Andrey", "email": "andrey@gmail.com"}
}


@app.post("/V1/register", tags=["Register"])
def register(usar_name: str, email: str, password: str):
    return {"message": "Registration successful"}


@app.get("/V1/user/{user_id}")
def read_user(user_id: str):
    if user_id in fake_users_db:
        return fake_users_db[user_id]
    else:
        raise HTTPException(status_code=404, detail="User not found")
