import unittest
import calc

class TestParts(unittest.TestCase):
    calc.readFile('test.txt')
    def test_part1(self):
        self.assertEqual(calc.part1(), 2028)
    def test_part12(self):
        calc.readFile('test2.txt')
        self.assertEqual(calc.part1(), 10092)
    def test_part2(self):
        calc.readFile('test2.txt')
        self.assertEqual(calc.part2(), 9021)

if __name__ == "__main__":
    unittest.main()
