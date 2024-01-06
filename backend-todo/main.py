from typing import Union

from fastapi import FastAPI
from schema import UserDetails
from models import User
from db import session

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Path parameter
@app.post("/login")
def login(user: UserDetails):
    user = User(
        email = user.email,
        password = user.password
    )

    session.add(user)
    session.commit()
    users = session.query(User).all()
    print("ALl users", users)
    return {"email": user.email, "password": user.password}

# Query Parameter
@app.post("/signup")
def signup(login_details: UserDetails):
    return "Signed Up"

