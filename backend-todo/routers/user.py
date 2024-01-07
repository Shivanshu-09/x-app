from typing import Union
import jwt

from fastapi import APIRouter
from schema import UserDetails
from models import User
from db import session
from datetime import datetime, timedelta

router = APIRouter()

# Secret key to sign and verify JWT tokens
SECRET_KEY = "x-app"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_jwt_token(login_details):
    data = {
        "email" : login_details.email,
        "password": login_details.password
    }
    expire = datetime.utcnow() + timedelta(days=1)
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Path parameter
@router.post("/login")
def login(user: UserDetails):
    logged_user = session.query(User).filter_by(email = user.email, password = user.password).all()
    if logged_user:
        jwt_token = create_jwt_token(user)
        return {"access_token": jwt_token}
    else:
        return "Invalid User"
    

# Query Parameter
@router.post("/signup")
def signup(login_details: UserDetails):
    email = login_details.email
    user = session.query(User).filter_by(email = email).all()
    if user:
        return "User is already signed Up"
    else:
        user = User(
            email = login_details.email,
            password = login_details.password
        )
        session.add(user)
        session.commit()

    jwt_token = create_jwt_token(login_details)
    return {"access_token": jwt_token}
    

