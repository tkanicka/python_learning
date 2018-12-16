import unittest
from ToRoman import ToRoman as func


class TestToRoman(unittest.TestCase):

    def test_input(self):
        self.assertRaises(ValueError, func, 0)
        self.assertRaises(ValueError, func, 56.35)
        self.assertRaises(ValueError, func, -7)
        self.assertRaises(ValueError, func, 4500)

    def test_figures(self):
        self.assertEqual(func(4), "IV")
        self.assertEqual(func(9), "IX")
        self.assertEqual(func(10), "X")
        self.assertEqual(func(3), "III")
        self.assertEqual(func(7), 'VII')

    def test_decimals(self):
        self.assertEqual(func(44), "XLIV")
        self.assertEqual(func(50), "L")
        self.assertEqual(func(33), "XXXIII")
        self.assertEqual(func(74), "LXXIV")
        self.assertEqual(func(99), "XCIX")

    def test_hundreds(self):
        self.assertEqual(func(100), "C")
        self.assertEqual(func(500), "D")
        self.assertEqual(func(444), "CDXLIV")
        self.assertEqual(func(999), "CMXCIX")
        self.assertEqual(func(357), "CCCLVII")
        self.assertEqual(func(689), "DCLIIIIX")

    def test_thousands(self):
        self.assertEqual(func(1000), "M")
        self.assertEqual(func(3394), "MMMCCCXCIV")
        self.assertEqual(func(1947), "MCMXLVII")
        self.assertEqual(func(3444), "MMMCDXLIV")
        self.assertEqual(func(1555), "MDLV")
        self.assertEqual(func(3999), "MMMCMXCIX")


if __name__ == "__main__":
    unittest.main()