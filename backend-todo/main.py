from fastapi import FastAPI
from routers import todo, user
app = FastAPI()

app.include_router(todo.router)
app.include_router(user.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}

