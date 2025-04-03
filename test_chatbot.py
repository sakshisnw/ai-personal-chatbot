import unittest
from chatbot import get_response

class TestChatbot(unittest.TestCase):
    def test_response(self):
        response = get_response("Hello")
        self.assertTrue(len(response) > 0)

if __name__ == "__main__":
    unittest.main()
