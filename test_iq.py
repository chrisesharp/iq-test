import unittest
from iq_test import iq_test

class IQTest(unittest.TestCase):
    def test_7_as_odd_one_out(self):
        self.assertEqual(3, iq_test("2 4 7 8 10"))
    
    def test_3_as_odd_one_out(self):
        self.assertEqual(2, iq_test("2 3 4 8 10"))
    
    def test_first_as_odd_one_out(self):
        self.assertEqual(1, iq_test("1 2 2"))
    
    def test_last_as_odd_one_out(self):
        self.assertEqual(3, iq_test("2 4 5"))
    
    def test_4_as_odd_one_out(self):
        self.assertEqual(3, iq_test("1 3 4 5 7"))
    

