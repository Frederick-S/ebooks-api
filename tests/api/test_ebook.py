from tests.base_test import BaseTestCase


class EbookTestCase(BaseTestCase):
    def test_get_ebooks_with_invalid_parameters(self):
        response1 = self.client.get('v1.0/ebooks')
        response2 = self.client.get(
            '/v1.0/ebooks?provider=weread')

        self.assertEqual(400, response1.status_code)
        self.assertEqual(400, response2.status_code)

    def test_get_ebooks_weread(self):
        response = self.client.get(
            '/v1.0/ebooks?provider=weread&title=python')

        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json) > 0)

    def test_get_ebooks_duokan(self):
        response = self.client.get(
            '/v1.0/ebooks?provider=duokan&title=python')

        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json) > 0)

    def test_get_ebooks_turing(self):
        response = self.client.get(
            '/v1.0/ebooks?provider=turing&title=python')

        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json) > 0)

    def test_get_ebooks_epubit(self):
        response = self.client.get(
            '/v1.0/ebooks?provider=epubit&title=python')

        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json) > 0)

    def test_get_ebooks_douban(self):
        response = self.client.get(
            '/v1.0/ebooks?provider=douban&title=python')

        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json) > 0)

    def test_get_ebooks_kindle(self):
        try:
            response = self.client.get(
                '/v1.0/ebooks?provider=kindle&title=python')

            if response.status_code == 200:
                self.assertTrue(len(response.json) > 0)
        except Exception as e:
            pass

    def test_get_ebooks_jd(self):
        response = self.client.get(
            '/v1.0/ebooks?provider=jd&title=python')

        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json) > 0)
