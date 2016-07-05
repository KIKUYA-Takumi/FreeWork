import unittest
import TestPractice

class TestCalc(unittest.TestCase):

    def test_add_three(self):
        self.assertEqual(TestPractice.add_three(5),8)

    def test_input_text(self):
        self.assertEqual(TestPractice.input_text(test),test)