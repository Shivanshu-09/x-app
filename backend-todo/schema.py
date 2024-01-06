from pydantic import BaseModel

class UserDetails(BaseModel):
    email : str
    password: str
