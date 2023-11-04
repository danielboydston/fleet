from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from .db import engine, create_db_and_tables, create_static_data
from .models import User
import logging

app = FastAPI(
    title="Fleet API",
    description="Fleet tracking for all kinds of equipment",
    version="0.1.0"
)

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://fleet.airwarrior.net",
    "https://fleet.airwarrior.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def main():
    return {"detail": "Welcome!"}

@app.get("/user/{user_id}")
async def getUser(user_id):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()
    return user


@app.get("/db/create-static-data")
async def static_data():
    logging.info("main.py.create_static_data()")
    create_static_data()
    return {"success": True}