import unittest
import calc

class TestParts(unittest.TestCase):
    calc.readFile('test.txt')
    def test_part1(self):
        # self.assertEqual(calc.part1(), 140)
        self.assertEqual(calc.part1(), 772)
    def test_part2(self):
        # self.assertEqual(calc.part2(), 80)
        self.assertEqual(calc.part2(), 436)
        # self.assertEqual(calc.part2(), 236)
        # self.assertEqual(calc.part2(), 368)

if __name__ == "__main__":
    unittest.main()
