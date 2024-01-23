import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_login_success(self):
        response = self.app.post('/login', data={'username': 'admin', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Login successful')

    def test_login_failure(self):
        response = self.app.post('/login', data={'username': 'admin', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Login failed')


if __name__ == '__main__':
    unittest.main()