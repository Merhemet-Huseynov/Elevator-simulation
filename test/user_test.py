import sys
import os

# File path
sys.path.append(os.path.abspath("../"))

from user import User
import unittest

class TestUser(unittest.TestCase):
    
    def test_generate_user_count(self):
        user = User()
        result = user.generate_user_count()
        user_count = len(result.split())
        self.assertIn(user_count, [1, 2, 3])
    
    def test_current_floor(self):
        user = User()
        result = user.current_floor(10)
        self.assertIn(result, range(1, 11))  
    
    def test_target_floor(self):
        user = User()
        result = user.target_floor(10)
        self.assertIn(result, range(1, 11))

if __name__ == "__main__":
    unittest.main()
