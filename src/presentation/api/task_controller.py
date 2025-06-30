from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from domain.entities.task import TaskStatus
from deps import get_task_service
from presentation.responses.response import SuccessResponse

router = APIRouter()


@router.post("/tasks")
def create_task(
    title: str,
    description: str,
    due_date: datetime,
    priority: int,
    service=Depends(get_task_service),
):
    if (
        due_date < datetime.now(tz=due_date.tzinfo)
        if due_date.tzinfo
        else datetime.now()
    ):
        raise HTTPException(status_code=400, detail="Due date cannot be in the past")

    try:
        task = service.create_task.execute(title, description, due_date, priority)
        return SuccessResponse(data=task)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/tasks/{task_id}/status")
def update_status(task_id: str, status: TaskStatus, service=Depends(get_task_service)):
    task = service.update_status.execute(task_id, status)
    return SuccessResponse(
        message=f"Task with id {task_id} updated successfully", data=task
    )


@router.delete("/tasks/{task_id}")
def delete_task(task_id: str, service=Depends(get_task_service)):
    service.delete_task.execute(task_id)
    return SuccessResponse(message=f"Task with id {task_id} deleted successfully")


@router.post("/tasks/{task_id}/assign")
def assign_task(task_id: str, user_id: str, service=Depends(get_task_service)):
    task = service.assign_task(task_id, user_id)
    return SuccessResponse(
        message=f"Task with id {task_id} assigned successfully to user with id {user_id}",
        data=task,
    )


@router.get("/tasks")
def get_all(service=Depends(get_task_service)):
    tasks = service.get_all_tasks()
    return SuccessResponse(data=tasks)


@router.get("/tasks/user/{user_id}")
def get_by_user(user_id: str, service=Depends(get_task_service)):
    tasks = service.get_tasks_by_user(user_id)
    return SuccessResponse(data=tasks)
