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

    def test_average_not_equal(self):
        self.assertNotEqual(99, a.average([91, 88, 96, 81]))

    def test_average_floats(self):
        self.assertEqual(89.88, a.average([92.3, 91.6, 89.2, 86.4]))

    def test_average_not_equal_floats(self):
        self.assertNotEqual(91.34, a.average([99.4, 87.5, 93.1]))


if __name__ == '__main__':
    unittest.main()
"""My unit tests are testing for equal and not equal
    with int and floating point values.
    I added round 2 to my average() because my 
    tests were not rounding up as my function was.
"""
