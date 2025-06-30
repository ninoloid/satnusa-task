from infrastructure.repositories.in_memory_task_repo import InMemoryTaskRepository
from application.services.task_service import TaskService

repo = InMemoryTaskRepository()
task_service = TaskService(repo)


def get_task_service():
    return task_service
