from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    # ใส่เพิ่มต่อท้ายเข้าไป
    def mark_as_complete(self, task_id: int):
        task = self.repository.update(task_id, True)
        if not task:
            raise Exception("ไม่พบงานที่ต้องการอัปเดต")
        return task