"""
write full unitest for ../mental_server.py
"""

"""
write full unitest for ../mental_server.py
"""

import unittest
from fastapi.testclient import TestClient
from mental_server import app

class MentalServerTestCase(unittest.TestCase):
    """
    Test case for the MentalServer application.
    """
    def setUp(self):
        self.client = TestClient(app)
        self.app = app
        self.app.testing = True

    def test_test_endpoint(self):
        response = self.client.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('line', response.json)

    def test_predict_endpoint(self):
        response = self.client.post('/predict', json={'text': 'I feel happy today!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('classification', response.json)

    def test_predict_endpoint_with_anxiety(self):
        response = self.client.post('/predict', json={'text': 'I am very anxious about my exams.'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['classification'], 'Anxiety')

    def test_predict_endpoint_with_depression(self):
        response = self.client.post('/predict', json={'text': 'I feel so down and hopeless.'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['classification'], 'Depression')

    def test_predict_endpoint_with_neutral(self):
        response = self.client.post('/predict', json={'text': 'I am feeling neutral today.'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['classification'], 'Neutral')

if __name__ == '__main__':
    unittest.main()