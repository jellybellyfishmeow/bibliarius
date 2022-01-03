from unittest.mock import patch

from parameterized import parameterized
from fastapi.testclient import TestClient

from bibliarius.main import APP
from bibliarius.routers.models import HealthStatus

from tests.base import BibliariusTest


class MainTest(BibliariusTest):
    """
    Test Main APP module
    """

    def setUp(self) -> None:
        """
        Setup test client
        """

        super().setUp()
        self.client = TestClient(APP)

    @parameterized.expand(
        [
            (True, "HEALTHY"),
            (False, "FAILING"),
        ]
    )
    def test_healthcheck(self, db_check_result: bool, expected_status: str) -> None:
        """
        Test /healthz endpoint
        """
        mock_db_check = patch("bibliarius.main.verify_db_connection").start()
        mock_db_check.return_value = db_check_result

        expected = HealthStatus(status=expected_status).dict()

        actual = self.client.get("/healthz").json()

        self.assertDictEqual(expected, actual)
        mock_db_check.assert_called_once_with()
