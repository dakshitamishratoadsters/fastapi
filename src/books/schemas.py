from pydantic import BaseModel 
from sqlmodel import SQLModel
from datetime import date

class Book(BaseModel):
    id : int
    title: str
    author :str 
    published_year: int
    page_count: int
    language : str

class BookUpdateModel (BaseModel):
    title :str
    author: str
    published_year: int
    page_count: int
    language : str

  
    
class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str

