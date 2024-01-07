from pydantic import BaseModel

class UserDetails(BaseModel):
    email : str
    password: str

class Todos(BaseModel):
    title : str
    description : str