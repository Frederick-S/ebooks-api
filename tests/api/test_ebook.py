from tests.base_test import BaseTestCase


class NotebookTestCase(BaseTestCase):
    def test_get_ebooks(self):
        response = self.client.get(
            '/api/v1/ebooks?provider=weread&book_name=python')

        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json) > 0)
