from domain.repositories.task_repository import ITaskRepository
from domain.entities.task import Task
from typing import List


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = {}

    def add(self, task: Task):
        self.tasks[task.id] = task

    def update(self, task: Task):
        self.tasks[task.id] = task

    def delete(self, task_id: str):
        self.tasks.pop(task_id, None)

    def get_all(self) -> List[Task]:
        return list(self.tasks.values())

    def get_by_user(self, user_id: str) -> List[Task]:
        return [t for t in self.tasks.values() if t.assigned_to == user_id]

    def get(self, task_id: str) -> Task | None:
        return self.tasks.get(task_id)
