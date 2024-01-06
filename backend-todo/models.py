from sqlalchemy import Column, Integer, String, DateTime, Text, BigInteger
from sqlalchemy.orm import declarative_base
from datetime import datetime
from time import time

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    _id = Column(Integer(), primary_key=True)
    email = Column(String(24), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    created = Column(BigInteger, default=time)
    updated = Column(BigInteger, default=time, onupdate=time)
    