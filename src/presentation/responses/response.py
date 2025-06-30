from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    error: bool = False
    code: int = 200
    message: str = "Success"
    data: Optional[T] = None


class GeneralErrorResponse(BaseModel):
    error: bool = True
    code: int = 500
    message: str = "Internal Server Error"
    data: Optional[T] = None
