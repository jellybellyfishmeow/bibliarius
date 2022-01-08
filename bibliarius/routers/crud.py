from sqlalchemy.orm import Session
from bibliarius.routers.models import Book as apiBook  #model
from bibliarius.data.models import Book as SqlBook # schema

def get_book_by_isbn(db: Session, isbn: int):
    return db.query(SqlBook).filter(SqlBook.isbn == isbn).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SqlBook).offset(skip).limit(limit).all()

def create_book(db: Session, book: apiBook.BookCreate):
    db_book = apiBook.Book()
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book