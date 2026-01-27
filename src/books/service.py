from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.models import Book
from src.books.schemas import BookCreateModel
from sqlmodel import desc, select



class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result =await session.exec(statement)
        return result.all()
    
    async def create_book(self,book_data:BookCreateModel,session:AsyncSession):
        book_data =book_data.model_dump()
        new_book = Book(
            **book_data_dict
            )


