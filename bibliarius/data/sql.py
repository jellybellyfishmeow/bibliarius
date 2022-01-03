from os import environ
from typing import Generator

from psycopg2 import DatabaseError
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from bibliarius.logging import get_logger

_PSQL_DB = environ.get("PSQL_DB", "bibliarius")
_PSQL_DIALECT = "psycopg2"
_PSQL_PASS = environ.get("PSQL_PASS", "muppetverseofmadness")
_PSQL_SERVER = environ.get("PSQL_SERVER", "localhost:5432")
_PSQL_USER = environ.get("PSQL_USER", "pblubbs")

_DATABASE_URL = f"postgresql+{_PSQL_DIALECT}://{_PSQL_USER}:{_PSQL_PASS}@{_PSQL_SERVER}/{_PSQL_DB}"

_LOGGER = get_logger(__name__)

_SQL_ENGINE = create_engine(
    url=_DATABASE_URL,
    # https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine.params
    pool_pre_ping=True,
    pool_size=10,
    pool_recycle=3600,
    pool_timeout=0.1,
    isolation_level="READ COMMITTED",
)

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#using-a-sessionmaker
_SQL_SESSION_FACTORY = sessionmaker(
    bind=_SQL_ENGINE,
    expire_on_commit=True,
)

SQL_BASE = declarative_base(
    bind=_SQL_ENGINE,
    name="SQL_BASE",
)


def get_db_session() -> Generator[Session, None, None]:
    """
    Fetch SQL Session
    """

    _LOGGER.debug("Fetching new PSQL session...")
    session = _SQL_SESSION_FACTORY()
    try:
        yield session
    finally:
        _LOGGER.debug("Closing PSQL session...")
        session.close()


def verify_db_connection() -> bool:
    """
    Verifies working SQL connections
    """

    try:
        with _SQL_ENGINE.connect() as conn:
            is_connected = not conn.closed
    except DatabaseError as err:
        _LOGGER.exception(f"PSQL connection failed: {err}")
        is_connected = False
    return is_connected
