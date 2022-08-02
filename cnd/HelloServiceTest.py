#!/usr/bin/env python3
"""HelloServiceTest.py
"""

import unittest
import requests

class HelloServiceTest(unittest.TestCase):
    def setUp(self):
        self.response = requests.get("http://127.0.0.1:8888")

    def testStatus(self):
        self.assertEqual(self.response.status_code, 200)

    def testContentType(self):
        self.assertEqual(self.response.headers["Content-Type"], "application/json")
    
    def testResponse(self):
        self.assertEqual(self.response.json()["message"], "Hello world")

if __name__ == "__main__":
    unittest.main()