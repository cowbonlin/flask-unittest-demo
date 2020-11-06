import unittest

from app import create_app, socketio

class FlaskTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.ctx = self.app.app_context()
        self.ctx.push()
        self.client = self.app.test_client() # for HTTP requests

    def tearDown(self):
        self.ctx.pop()

    def test_helloword(self):
        response = self.client.get('/helloword')
        self.assertEqual(response.status_code, 200)
        data = response.get_data(as_text=True)
        self.assertEqual(data, 'greeting from cowbon')

    def test_socketio(self):
        client = socketio.test_client(self.app)
        response = client.emit('some_event', {}, callback=True)
        self.assertEqual(response['status'], 0)
