import pytest
from datetime import datetime, timedelta
from domain.entities.task import TaskStatus
from application.services.task_service import TaskService
from infrastructure.repositories.in_memory_task_repo import InMemoryTaskRepository


@pytest.fixture
def service():
    repo = InMemoryTaskRepository()
    return TaskService(repo)


def test_create_task_success(service):
    task = service.create_task.execute(
        title="Test Task",
        description="Testing",
        due_date=datetime.now() + timedelta(days=1),
        priority=2,
    )
    assert task.title == "Test Task"
    assert task.status == TaskStatus.PENDING


def test_update_task_status(service):
    task = service.create_task.execute(
        title="Task to update",
        description="Status update",
        due_date=datetime.now() + timedelta(days=2),
        priority=1,
    )
    updated = service.update_status.execute(task.id, TaskStatus.COMPLETED)
    assert updated.status == TaskStatus.COMPLETED


def test_delete_task(service):
    task = service.create_task.execute(
        title="To Delete",
        description="Will be deleted",
        due_date=datetime.now() + timedelta(days=1),
        priority=1,
    )
    service.delete_task.execute(task.id)
    assert service.repo.get(task.id) is None


def test_assign_task(service):
    task = service.create_task.execute(
        title="Assign Me",
        description="Assign test",
        due_date=datetime.now() + timedelta(days=1),
        priority=3,
    )
    assigned = service.assign_task(task.id, user_id="user123")
    assert assigned.assigned_to == "user123"


def test_get_all_tasks(service):
    service.create_task.execute("T1", "Desc1", datetime.now() + timedelta(days=1), 1)
    service.create_task.execute("T2", "Desc2", datetime.now() + timedelta(days=1), 2)
    tasks = service.get_all_tasks()
    assert len(tasks) == 2


def test_get_tasks_by_user(service):
    t1 = service.create_task.execute(
        "U1-T1", "Desc", datetime.now() + timedelta(days=1), 1
    )
    t2 = service.create_task.execute(
        "U1-T2", "Desc", datetime.now() + timedelta(days=1), 1
    )
    service.assign_task(t1.id, "user1")
    service.assign_task(t2.id, "user1")

    user_tasks = service.get_tasks_by_user("user1")
    assert len(user_tasks) == 2
