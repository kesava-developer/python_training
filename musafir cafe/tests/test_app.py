import unittest

from app import app


class CafeAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page_renders(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_returns_packages(self):
        response = self.client.get('/api/cafe-types')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertGreaterEqual(len(data), 3)

    def test_enroll_endpoint(self):
        response = self.client.post('/api/enroll', json={
            'name': 'Asha',
            'email': 'asha@example.com',
            'package': 'Velvet Cappuccino'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.get_json()['ok'])


if __name__ == '__main__':
    unittest.main()
