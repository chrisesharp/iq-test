import unittest

def iq_test(string_of_numbers):
    return 3

class IQTest(unittest.TestCase):
    def test_odd_one_out(self):
        self.assertEqual(2, iq_test("2 4 7 8 10"))
