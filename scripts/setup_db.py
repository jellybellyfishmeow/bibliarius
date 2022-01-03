from datetime import date

from bibliarius.data.sql import get_db_session, verify_db_connection
from bibliarius.data.models import Book, SQL_BASE
from bibliarius.logging import get_logger

_LOGGER = get_logger(__name__)

_BOOKS = (
    Book(
        isbn="978-1492055020",
        title="High Performance Python: Practical Performant Programming for Humans 2nd Edition",
        author="Micha Gorelick, Ian Ozsvald",
        description=(
            "Your Python code may run correctly, but you need it to run faster. "
            "Updated for Python 3, this expanded edition shows you how to locate performance bottlenecks "
            "and significantly speed up your code in high-data-volume programs. "
            "By exploring the fundamental theory behind design choices, High Performance Python helps you "
            "gain a deeper understanding of Python's implementation."
        ),
        publish_date=date(
            day=26,
            month=5,
            year=2020,
        ),
    ),
    Book(
        isbn="978-1492052203",
        title=(
            "Architecture Patterns with Python: Enabling Test-Driven Development, "
            "Domain-Driven Design, and Event-Driven Microservices 1st Edition"
        ),
        author="Harry Percival, Bob Gregory",
        description=(
            "As Python continues to grow in popularity, projects are becoming larger and more complex. "
            "Many Python developers are taking an interest in high-level software design patterns "
            "such as hexagonal/clean architecture, event-driven architecture, and the strategic patterns "
            "prescribed by domain-driven design (DDD)."
        ),
        publish_date=date(
            day=31,
            month=3,
            year=2020,
        ),
    ),
)


def _db_setup():
    """
    Ensure a clean SQL DB is setup and ready to use
    """

    _LOGGER.info("Checking DB connection...")
    if not verify_db_connection():
        raise RuntimeError("Invalid DB Connection!")

    _LOGGER.info("Drop all tables...")
    SQL_BASE.metadata.drop_all()
    _LOGGER.info("Create all tables...")
    SQL_BASE.metadata.create_all()
    _LOGGER.info("DB tables setup.")

    _LOGGER.info("Inserting test data...")
    db_session = next(get_db_session())
    db_session.add_all(_BOOKS)
    db_session.commit()
    _LOGGER.info("Test DB data setup.")


_db_setup()
