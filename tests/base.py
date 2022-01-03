from unittest import TestCase


class BibliariusTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.maxDiff = None

    def tearDown(self) -> None:
        super().tearDown()
