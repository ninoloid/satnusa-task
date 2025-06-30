from domain.entities.task import TaskStatus
from fastapi import HTTPException


class UpdateTaskStatusUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, task_id: str, status: TaskStatus):
        task = self.repo.get(task_id)

        if not task:
            raise HTTPException(400, "Task not found")

        task.status = status
        self.repo.update(task)
        return task
