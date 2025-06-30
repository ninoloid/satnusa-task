from abc import ABC, abstractmethod
from typing import List
from domain.entities.task import Task


class ITaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task):
        pass

    @abstractmethod
    def update(self, task: Task):
        pass

    @abstractmethod
    def delete(self, task_id: str):
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def get_by_user(self, user_id: str) -> List[Task]:
        pass

    @abstractmethod
    def get(self, task_id: str) -> Task | None:
        pass
