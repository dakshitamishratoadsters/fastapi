from sqlmodel import SQLModel,Field ,Column,String
import sqlalchemy.dialects.postgresql as pg
import uuid

class Book(SQLModel,table=True):
    __tablename__ ="books" 
    uid:uuid.UUID=Field(
        sa_column=Column(
            pg.UUID,
            primary_key =True,
            unique=True,
            Nullable=False
        )
    )
    title:str
    author:str
    page_count:int
    published_year:int
    language:str



def __repr__(self) -> str:
        return f"<Book {self.title}>"
