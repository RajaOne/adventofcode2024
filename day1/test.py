import unittest
import part1

class TestParts(unittest.TestCase):
    part1.readFile('test.txt')
    def test_part1(self):
        self.assertEqual(part1.part1(), 11)
    def test_part2(self):
        self.assertEqual(part1.part2(), 31)


if __name__ == "__main__":
    unittest.main()


