from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Task, TaskCreate

class ITaskRepository(ABC):
   

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task:
        pass
        
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def update(self, task_id: int, is_completed: bool):
        pass

class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = []
        self.current_id = 1
   
    def get_all(self) -> List[Task]:
        return self.tasks

    def create(self, task_in: TaskCreate) -> Task:
        task = Task(
            id=self.current_id,
            **task_in.dict()
        )
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
from sqlalchemy.orm import Session
from . import models_orm  # ต้องสร้าง SQLAlchemy Model แยก

class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    # ... ฟังก์ชัน get หรือ create เดิม ...

    # ใส่เพิ่มต่อท้ายเข้าไป
    def update(self, task_id: int, is_completed: bool):
        # 1. ค้นหา Task จาก ID
        db_task = self.db.query(models_orm.TaskModel).filter(models_orm.TaskModel.id == task_id).first()
        if db_task:
            # 2. แก้ค่าสถานะ
            db_task.completed = is_completed 
            # 3. สั่งให้บันทึกลงไฟล์ .db จริงๆ (ถ้าไม่มีบรรทัดนี้ ข้อมูลจะไม่ขึ้นใน SQL)
            self.db.commit() 
            self.db.refresh(db_task)
        return db_task
    
    def update_task_complete(self, task_id: int, is_completed: bool):
        db_task = self.db.query(models_orm.Task).filter(models_orm.Task.id == task_id).first()
        if db_task:
            db_task.completed = is_completed
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    def get_by_id(self, id: int):
        return self.db.query(models_orm.Task).filter(models_orm.Task.id == id).first()
    