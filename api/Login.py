from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str

def index(age: int):
    return {"fun": "index", "age": age}

def login(data: Login):
    return data