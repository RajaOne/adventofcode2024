import unittest
import calc

class TestParts(unittest.TestCase):
    def test_part1(self):
        calc.readFile('test.txt')
        self.assertEqual(calc.part1(), 161)
    def test_part2(self):
        calc.readFile('test2.txt')
        self.assertEqual(calc.part2(), 48)

if __name__ == "__main__":
    unittest.main()
