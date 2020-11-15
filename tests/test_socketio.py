import unittest

from app import create_app, socketio

class SocketioTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_socketio(self):
        client = socketio.test_client(self.app)
        response = client.emit('some_event', {'from': 'unittest'}, callback=True)
        self.assertEqual(response['status'], 0)
