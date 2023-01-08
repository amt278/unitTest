'''        to run test in terminal: python -m unittest filename             '''

import unittest
import main

class test(unittest.TestCase):
    def test_with_one_digit(self):
        self.assertEqual(main.length(1), 1)
        

    def test_with_more_than_one_digit(self):
        self.assertEqual(main.length(17), 2)

