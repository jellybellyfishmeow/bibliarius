from typing import Literal

from pydantic import BaseModel


class HealthStatus(BaseModel):
    """
    Health Check Payload
    """

    status: Literal["HEALTHY", "FAILING"]


class Book(BaseModel):
    isbn: str
    title: str
    author: str
    description: str
    publish_date: str

    class Config:
        orm_mode = True

class BookCreate(BaseModel):
    isbn: str
    title: str
    author: str
    description: str
    publish_date: str