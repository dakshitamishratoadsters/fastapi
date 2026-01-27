from fastapi import APIRouter ,status , HTTPException
from src.books.book_data import books
from src.books.schemas import Book,BookUpdateModel
from typing import List , Dict



book_router = APIRouter()

@book_router.get("/books",response_model=list[Book])
async def get_all_books():
    return books

@book_router.post("/books",status_code= status.HTTP_201_CREATED,response_model=Book)
async def add_book(book_data : Book):
    new_book =book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get("/books/{book_id}",response_model=Book)
async def get_book_by_id(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
        
    raise HTTPException(status_code=404, details ="Book not found")
   
        
@book_router.patch("/books/{book_id}",response_model=Book)
async def update_book(book_id:int ,book_update_model:BookUpdateModel):
    for book in books:
        b_id = book.get("id",None)
        if b_id and b_id ==book_id:
            book["title"] = book_update_model.title
            book["author"]=book_update_model.auhtor
            book["published_year"]= book_update_model.published_year
            book["page_count"]= book_update_model.page_count
            book["language"]= book_update_model.language
            return book
    raise HTTPException (status_code=404, detail="Book not found")

@book_router.delete("/books/{book_id}",response_model=Dict[str,str])
async def delete_book(book_id:int):
    for book in books:
        b_id =book.get("id",None)
        if b_id and b_id == book_id:
            book.remove(book)
            return {"message: book deleted successfully"}
        
        raise HTTPException(status_code = 404 ,detail ="book not found")
