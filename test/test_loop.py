"""Author: Michael Harmon
   Last Date Modified: 9/19/2019
   Description: These unit tests will
   test the average_scores function.
"""

import unittest
from input_loops import average_input_scores as a


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(93.75, a.average([95, 99, 93, 88]))


if __name__ == '__main__':
    unittest.main()
