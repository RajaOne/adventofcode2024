import unittest
import calc

class TestParts(unittest.TestCase):
    calc.readFile('test.txt')
    def test_part1(self):
        self.assertEqual(calc.part1(), 55312)
    def test_part2(self):
        self.assertEqual(calc.part2(), 65601038650482)

if __name__ == "__main__":
    unittest.main()
