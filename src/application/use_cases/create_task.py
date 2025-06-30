import uuid
from domain.entities.task import Task, TaskStatus


class CreateTaskUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, title, description, due_date, priority):
        task = Task(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status=TaskStatus.PENDING,
        )
        self.repo.add(task)
        return task
