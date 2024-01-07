from sqlalchemy import Column, Integer, String, DateTime, Text, BigInteger, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from time import time

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    _id = Column(Integer(), primary_key=True)
    email = Column(String(24), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    todo = relationship('Todo', back_populates='user')
    created = Column(BigInteger, default=time)
    updated = Column(BigInteger, default=time, onupdate=time)

class Todo(Base):
    __tablename__ = 'todo'

    _id = Column(Integer(), primary_key=True)
    title = Column(String(255), nullable= False)
    description = Column(String(255), nullable=False)
    user_id = Column(Integer(), ForeignKey('user._id'))
    user = relationship('User', back_populates='todo')
    created = Column(BigInteger, default=time)
    updated = Column(BigInteger, default=time, onupdate=time)

    