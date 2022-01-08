"""
TODO:
/books router that
1) GET Books from DB (all or 1 by ISBN) -> /books + /books/{isbn}
2) POST new Book to DB -> /books
"""

from os import environ

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from typing import List
from bibliarius.logging import get_logger
from bibliarius.routers.models import Book as apiBook  #schema
from bibliarius.data.models import Book as SqlBook # model
from bibliarius.routers import crud
from bibliarius.data.sql import _SQL_SESSION_FACTORY, _SQL_ENGINE

SqlBook.Base.metadata.create_all(bind=_SQL_ENGINE)

APP = FastAPI(
    title="bibliarius",
    debug=environ.get("DEBUGGING", "false").lower() == "true",
)
_LOGGER = get_logger(__name__)

def get_db():
    db = _SQL_SESSION_FACTORY()
    try:
        yield db
    finally:
        db.close()

# create book 
@APP.post("/book/", response_model=apiBook)
def create_book(book: apiBook.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_isbn(db, isbn=book.isbn)
    if db_book:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_book(db=db, book=book)

# get all books
@APP.get("/book/", response_model=List[apiBook])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_books = crud.get_books(db, skip=skip, limit=limit)
    return db_books

# get by isbn
@APP.get("/book/{isbn}", response_model=apiBook)
def read_book(isbn: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_isbn(db, isbn=isbn)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book