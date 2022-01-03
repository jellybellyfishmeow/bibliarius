from sqlalchemy import Column, Date, String, Text

from bibliarius.data.sql import SQL_BASE


class Book(SQL_BASE):
    """
    Represents a unique book by ISBN
    """

    __tablename__ = "book"

    # 10 or 13 characters are both listed on Amazon
    isbn = Column(String(16), primary_key=True, index=True)
    title = Column(String(256), unique=False, nullable=False)
    author = Column(String(128), unique=False, nullable=False)
    description = Column(Text, unique=False, nullable=True)
    publish_date = Column(Date, unique=False, nullable=False)
