import unittest

def iq_test(string_of_numbers):
    odd_numbers = [int(x)%2!=0 for x in string_of_numbers.split()]
    odd_position = odd_numbers.index(True) + 1
    return odd_position

class IQTest(unittest.TestCase):
    def test_7_as_odd_one_out(self):
        self.assertEqual(3, iq_test("2 4 7 8 10"))
    
    def test_3_as_odd_one_out(self):
        self.assertEqual(2, iq_test("2 3 4 8 10"))
