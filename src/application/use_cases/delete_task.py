from fastapi import HTTPException


class DeleteTaskUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, task_id: str):
        task = self.repo.get(task_id)

        if not task:
            raise HTTPException(400, "Task not found")

        self.repo.delete(task_id)
        return None
