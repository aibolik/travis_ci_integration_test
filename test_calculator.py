import unittest

from new_calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_1(self):
        c = Calculator()
        self.assertEqual(c.display, "")

    def test_2(self):
        c = Calculator()
        c.press("1")
        c.press("2")
        c.press("C")
        self.assertEqual(c.display, "")

    def test_3(self):
        c = Calculator()
        c.press("1")
        self.assertEqual(c.display, "1")

    def test_4(self):
        c = Calculator()
        c.press("1")
        c.press("+")
        c.press("1")
        c.press("=")
        self.assertEqual(c.display, "2")

    def test_5(self):
        c = Calculator()
        c.press("1")  # 1
        c.press("+")  # 1+
        c.press("1")  # 1+1
        c.press("=")  # 2
        c.press("+")  # 2 +
        c.press("1")  # 2 + 1
        c.press("=")  # 3
        self.assertEqual(c.display, "3")

    def test_6(self):
        """1+1+1+2=5"""
        c = Calculator()
        c.press("1")
        c.press("+")
        c.press("1")
        c.press("+")
        c.press("1")
        c.press("+")
        c.press("2")
        c.press("=")
        self.assertEqual(c.display, "5")

    def test_7(self):
        """1+1+1+2=5"""
        c = Calculator()
        c.press("1")
        c.press("+")
        c.press("1")
        c.press("=")
        c.press("C")
        c.press("1")
        c.press("+")
        c.press("3")
        c.press("=")
        self.assertEqual(c.display, "4")

    def test_8(self):
        """1+53*44+9"""
        c = Calculator()
        c.press("1")
        c.press("+")
        c.press("5")
        c.press("3")
        c.press("*")
        c.press("4")
        c.press("4")
        c.press("+")
        c.press("9")
        c.press("=")
        self.assertEqual(c.display, "2342")

    def test_9(self):
        """10+30*2"""
        c = Calculator()
        c.press("1")
        c.press("0")
        c.press("+")
        c.press("3")
        c.press("0")
        c.press("*")
        c.press("2")
        c.press("=")
        self.assertEqual(c.display, "70")

    def test_10(self):
        """10*3+30*2+1+2"""
        c = Calculator()
        c.press("1")
        c.press("0")
        c.press("+")
        c.press("3")
        c.press("0")
        c.press("*")
        c.press("2")
        c.press("+")
        c.press("1")
        c.press("+")
        c.press("2")
        c.press("=")
        self.assertEqual(c.display, "73")


if __name__ == '__main__':
    unittest.main()
