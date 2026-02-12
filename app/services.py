from .repositories import ITaskRepository
from .models import TaskCreate
from fastapi import HTTPException, status


class TaskService:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def get_tasks(self):
        return self.repository.get_all()

    def create_task(self, task: TaskCreate):
        # Validation: prevent duplicate title
        existing = self.repository.get_by_title(task.title)
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="มี Task ที่ชื่อเดียวกันแล้ว")
        return self.repository.create(task)

    def mark_as_complete(self, task_id: int):
        task = self.repository.update(task_id, True)
        if not task:
            raise Exception("ไม่พบงานที่ต้องการอัปเดต")
        return task