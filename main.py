from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# タスクの形の定義
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# 一時的なタスクの保存場所（メモリ）
tasks = []

@app.get("/")
def read_root():
    return {"message": "Task App is running!"}

# タスクの一覧を見る機能
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# 新しいタスクを追加する機能
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# 指定したIDのタスクを削除する機能
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted successfully"}
    return {"error": "Task not found"}
app.post