from application.use_cases.create_task import CreateTaskUseCase
from application.use_cases.update_task import UpdateTaskStatusUseCase
from application.use_cases.delete_task import DeleteTaskUseCase
from fastapi import HTTPException


class TaskService:
    def __init__(self, repo):
        self.create_task = CreateTaskUseCase(repo)
        self.update_status = UpdateTaskStatusUseCase(repo)
        self.delete_task = DeleteTaskUseCase(repo)
        self.repo = repo

    def assign_task(self, task_id: str, user_id: str):
        task = self.repo.get(task_id)
        if not task:
            raise HTTPException(400, "Task not found")
        task.assigned_to = user_id
        self.repo.update(task)
        return task

    def get_all_tasks(self):
        return self.repo.get_all()

    def get_tasks_by_user(self, user_id: str):
        return self.repo.get_by_user(user_id)
