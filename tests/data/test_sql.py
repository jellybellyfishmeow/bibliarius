from unittest.mock import patch

from parameterized import parameterized
from psycopg2 import DatabaseError, OperationalError

from bibliarius.data.sql import get_db_session, verify_db_connection

from tests.base import BibliariusTest


class SqlTest(BibliariusTest):
    """
    Integration type test for SQL module
    """

    def test_verify_db_connection(self) -> None:
        is_db_connected = verify_db_connection()

        self.assertTrue(is_db_connected)

    @parameterized.expand(
        [
            (DatabaseError(),),
            (OperationalError(),),
        ]
    )
    def test_verify_db_connection_errors(self, sql_err) -> None:
        mock_engine = patch("bibliarius.data.sql._SQL_ENGINE").start()
        mock_engine.connect.side_effect = sql_err

        is_db_connected = verify_db_connection()

        self.assertFalse(is_db_connected)
        mock_engine.connect.assert_called_once_with()

    def test_get_db_session(self) -> None:
        generator = get_db_session()
        session = next(generator, None)

        self.assertIsNotNone(session)

        close_patch = patch.object(session, "close")
        mock_close = close_patch.start()
        generator.close()
        close_patch.stop()
        session.close()

        mock_close.assert_called_once_with()
