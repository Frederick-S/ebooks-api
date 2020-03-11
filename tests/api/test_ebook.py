from tests.base_test import BaseTestCase


class NotebookTestCase(BaseTestCase):
    def test_get_ebooks_with_invalid_parameters(self):
        response1 = self.client.get('/api/v1/ebooks')
        response2 = self.client.get(
            '/api/v1/ebooks?provider=weread')

        self.assertEqual(400, response1.status_code)
        self.assertEqual(400, response2.status_code)

    def test_get_ebooks_weread(self):
        response = self.client.get(
            '/api/v1/ebooks?provider=weread&book_name=python')

        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json) > 0)

    def test_get_ebooks_duokan(self):
        response = self.client.get(
            '/api/v1/ebooks?provider=duokan&book_name=python')

        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json) > 0)
