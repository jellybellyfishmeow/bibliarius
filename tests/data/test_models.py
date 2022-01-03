from datetime import date

from sqlalchemy.sql.expression import delete, select

from bibliarius.data.models import Book
from bibliarius.data.sql import get_db_session

from tests.base import BibliariusTest


class SqlModelsTest(BibliariusTest):
    """
    Integration type test for SQL Models
    """

    _TEST_BOOK = Book(
        isbn="9780135957059",
        title=("The Pragmatic Programmer: Your Journey To Mastery, " "20th Anniversary Edition (2nd Edition)"),
        author="David Thomas, Andrew Hunt",
        description=(
            "The Pragmatic Programmer is one of those rare tech books you'll read, "
            "re-read, and read again over the years. "
            "Whether you're new to the field or an experienced practitioner, "
            "you'll come away with fresh insights each and every time."
        ),
        publish_date=date(
            year=2019,
            month=9,
            day=1,
        ),
    )

    def test_book(self) -> None:
        expected = self._TEST_BOOK.__dict__
        db_session = next(get_db_session())
        # never committed, should not affect future tests
        db_session.add(self._TEST_BOOK)

        stmt = select(Book).where(Book.isbn == "9780135957059")
        saved_book: Book = db_session.execute(stmt).fetchone()[0]
        saved_book_dict = saved_book.__dict__
        saved_book_dict.pop("_sa_instance_state")

        self.assertDictEqual(expected, saved_book_dict)
