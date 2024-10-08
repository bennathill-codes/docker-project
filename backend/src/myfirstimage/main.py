from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    content: str

class TodoItemCreate(BaseModel):
    content: str

todos: List[TodoItem] = []
id_counter = 1

# Get all to-do items
@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return todos

# Create a new to-do item
@app.post("/todos", response_model=TodoItem)
def create_todo(todo_data: TodoItemCreate):
    global id_counter
    new_todo = TodoItem(id=id_counter, content=todo_data.content)
    todos.append(new_todo)
    id_counter += 1
    return new_todo

# Delete a to-do item by ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"detail": "To-do item deleted"}