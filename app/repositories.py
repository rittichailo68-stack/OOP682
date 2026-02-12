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
    def get_by_title(self, title: str) -> Optional[Task]:
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

    def get_by_title(self, title: str) -> Optional[Task]:
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def update(self, task_id: int, is_completed: bool):
        task = self.get_by_id(task_id)
        if task:
            task.completed = is_completed
        return task

from sqlalchemy.orm import Session
from . import models_orm  # ต้องสร้าง SQLAlchemy Model แยก

class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Task]:
        db_tasks = self.db.query(models_orm.Task).all()
        return [Task.from_orm(task) for task in db_tasks]

    def create(self, task: TaskCreate) -> Task:
        db_task = models_orm.Task(**task.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return Task.from_orm(db_task)

    def get_by_id(self, task_id: int) -> Optional[Task]:
        db_task = self.db.query(models_orm.Task).filter(models_orm.Task.id == task_id).first()
        if db_task:
            return Task.from_orm(db_task)
        return None

    def get_by_title(self, title: str) -> Optional[Task]:
        db_task = self.db.query(models_orm.Task).filter(models_orm.Task.title == title).first()
        if db_task:
            return Task.from_orm(db_task)
        return None

    def update(self, task_id: int, is_completed: bool) -> Optional[Task]:
        db_task = self.db.query(models_orm.Task).filter(models_orm.Task.id == task_id).first()
        if db_task:
            db_task.completed = is_completed
            self.db.commit()
            self.db.refresh(db_task)
            return Task.from_orm(db_task)
        return None
    