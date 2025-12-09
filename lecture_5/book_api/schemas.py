from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

    class Config:
        orm_mode = True