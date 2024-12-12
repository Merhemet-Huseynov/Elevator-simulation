import sys
import os

# File path
sys.path.append(os.path.abspath("../"))

from elevator import Elevator
import unittest

class TestElevator(unittest.TestCase):
    def setUp(self):
        self.elevator = Elevator()

    def test_move_floors_of_elevator(self):
        self.assertEqual(self.elevator.move_floors_of_elevator(5), [5, 4, 3, 2, 1])

if __name__ == "__main__":
    unittest.main()
