from enum import Enum
from datetime import datetime
from pydantic import BaseModel


class TaskStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class Task(BaseModel):
    id: str
    title: str
    description: str
    due_date: datetime
    priority: int
    status: TaskStatus
    assigned_to: str | None = None
