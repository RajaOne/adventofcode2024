import unittest
import calc

class TestParts(unittest.TestCase):
    calc.readFile('test.txt')
    # def test_part1(self):
    #     self.assertEqual(calc.part1(), 36)
    def test_part2(self):
        self.assertEqual(calc.part2(), 81)

if __name__ == "__main__":
    unittest.main()