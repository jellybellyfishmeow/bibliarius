from fastapi.testclient import TestClient
from bibliarius.data.models import HealthStatus

from bibliarius.main import APP

from tests.base import BibliariusTest


class MainTest(BibliariusTest):
    def setUp(self) -> None:
        super().setUp()
        self.client = TestClient(APP)

    def test_healthcheck(self) -> None:
        expected = HealthStatus(status="HEALTHY").dict()

        actual = self.client.get("/healthz").json()

        self.assertDictEqual(expected, actual)
