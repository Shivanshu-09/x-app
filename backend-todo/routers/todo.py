from fastapi import APIRouter
from models import Todo, User
from schema import Todos
from db import session

router = APIRouter()


@router.get('/todos')
def get_todos(id: int):
    todos = session.query(Todo).filter_by(_id = id).first()
    if todos:
        return {"todos" : todos}
    else:
        return "No todos"
    

@router.put('/todos/{todo_id}')
def update_todo(todo_id : int, update_todo : Todos):
    todo = session.query(Todo).filter_by(_id = todo_id).first()
    if not todo:
        return "Todo is invalid"
    
    todo.title = update_todo.title
    todo.description = update_todo.description
    session.commit()
    return "Todos Updated successfully"

    
@router.post('/todos/{id}')
def add_todos(id: int, todos : Todos):
    user = session.query(User).filter_by(_id = id).first()
    if not user:
        return "User Id invalid"
    
    todo = Todo(
        title = todos.title,
        description = todos.description
    )

    session.add(todo)
    session.commit()
    return "Todos successfully added"

