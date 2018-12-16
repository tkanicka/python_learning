import unittest
from toarabic import toarabic as func


class TestToRoman(unittest.TestCase):

    def test_input(self):
        self.assertRaises(ValueError, func, 0)
        self.assertRaises(ValueError, func, 56.35)
        self.assertRaises(ValueError, func, -7)
        self.assertRaises(ValueError, func, 4500)

    def test_figures(self):
        self.assertEqual(func("IV"), 4)
        self.assertEqual(func("IX"), 9)
        self.assertEqual(func("X"), 10)
        self.assertEqual(func("III"), 3)
        self.assertEqual(func("VII"), 7)

    def test_decimals(self):
        self.assertEqual(func("XLIV"), 44)
        self.assertEqual(func("L"), 50)
        self.assertEqual(func("XXXIII"), 33)
        self.assertEqual(func("LXXIV"), 74)
        self.assertEqual(func("XCIX"), 99)

    def test_hundreds(self):
        self.assertEqual(func("C"), 100)
        self.assertEqual(func("D"), 500)
        self.assertEqual(func("CDXLIV"), 444)
        self.assertEqual(func("CMXCIX"), 999)
        self.assertEqual(func("CCCLVII"), 357)
        self.assertEqual(func("DCLIIIIX"), 689)

    def test_thousands(self):
        self.assertEqual(func("M"), 1000)
        self.assertEqual(func("MMMCCCXCIV"), 3394)
        self.assertEqual(func("MCMXLVII"), 1947)
        self.assertEqual(func("MMMCDXLIV"), 3444)
        self.assertEqual(func("MDLV"), 1555)
        self.assertEqual(func("MMMCMXCIX"), 3999)


if __name__ == "__main__":
    unittest.main()