import unittest

def iq_test(string_of_numbers):
    odds = [int(x)%2!=0 for x in string_of_numbers.split()]
    return odds.index(True) + 1 if odds.count(True) == 1 else odds.index(False) + 1

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
    

