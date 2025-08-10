import unittest
import json
from app import routes
from flask import Flask

class ProgressApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(routes.bp)
        self.client = self.app.test_client()

    def test_set_and_get_progress(self):
        # Set progress
        response = self.client.post('/api/progress/12.2', json={"status": "In Progress"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "In Progress")
        # Get progress
        response = self.client.get('/api/progress/12.2')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "In Progress")

    def test_get_all_progress(self):
        self.client.post('/api/progress/12.2', json={"status": "In Progress"})
        self.client.post('/api/progress/12.3', json={"status": "Completed"})
        response = self.client.get('/api/progress')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["12.2"], "In Progress")
        self.assertEqual(data["12.3"], "Completed")

    def test_missing_status(self):
        response = self.client.post('/api/progress/12.4', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
