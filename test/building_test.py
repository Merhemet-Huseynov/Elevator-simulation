import sys
import os

# File path
sys.path.append(os.path.abspath("../"))

import unittest
from elevator_system import Building

class TestBuilding(unittest.TestCase):

    def test_number_of_floors(self):
        building = Building()

        self.assertEqual(building.number_of_floors, 15)

if __name__ == "__main__":
    unittest.main()
