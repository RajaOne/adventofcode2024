grid = []
obstructions = {}

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self): return f'({self.x}, {self.y})'
    def __eq__(self, other): return self.x == other.x and self.y == other.y
    def __hash__(self): return hash((self.x, self.y))
    def add(self, other): return Point(self.x + other.x, self.y + other.y)

right_dir = Point(1, 0)
left_dir = Point(-1, 0)
up_dir = Point(0, -1)
down_dir = Point(0, 1)

def readFile(filename):
    global grid
    grid = []
    file = open(filename, 'r')
    lines = file.read().splitlines()
    [grid.append([c for c in line]) for line in lines]
    file.close()

def part1():
    p = findPlayer()
    grid[p.y][p.x] = 'X'
    traverse(p)
    return sum([line.count('X') for line in grid])

def turnRight(d):
    if d == up_dir: return right_dir
    if d == right_dir: return down_dir
    if d == down_dir: return left_dir
    return up_dir

def traverse(p):
    d = up_dir
    while True:
        next_p = p.add(d)
        if outside_grid(next_p): return
        c = grid[next_p.y][next_p.x]
        if c == '#':
            d = turnRight(d)
            continue
        if c == '.' or c == '^' or c == 'X':
            p = next_p
            grid[p.y][p.x] = 'X'

def traverse_with_dir(p):
    start_p = Point(p.x, p.y)
    d = up_dir
    counter = 0
    while True:
        counter += 1
        if counter%100 == 0: print(f'counter: {counter}/5700')
        next_p = p.add(d)
        if outside_grid(next_p): return
        c = grid[next_p.y][next_p.x]
        if c == '#':
            d = turnRight(d)
            continue
        if c in ('.', '^'):
            p = next_p
            if is_euclidean(p, start_p):
                obstructions[p] = True

def outside_grid(p):
    return p.y < 0 or p.y >= len(grid) or p.x < 0 or p.x >= len(grid[p.y])

def is_euclidean(p, start_p):
    test_start_p = Point(start_p.x, start_p.y)
    test_d = Point(up_dir.x, up_dir.y)
    test_grid = []
    test_dirs = []
    [test_grid.append([c for c in line]) for line in grid]
    [test_dirs.append([[] for c in line]) for line in grid]
    test_grid[p.y][p.x] = '#'
    test_dirs[test_start_p.y][test_start_p.x].append(Point(test_d.x, test_d.y))
    while True:
        next_p = test_start_p.add(test_d)
        if outside_grid(next_p):
            return False
        c = test_grid[next_p.y][next_p.x]
        if c == '#':
            test_d = turnRight(test_d)
            continue
        if test_d in test_dirs[next_p.y][next_p.x]:
            return True
        test_start_p = next_p
        test_dirs[test_start_p.y][test_start_p.x].append(Point(test_d.x, test_d.y))

def findPlayer():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                return Point(j, i)
    raise Exception('Player not found')

def part2():
    p = findPlayer()
    traverse_with_dir(p)
    return len(obstructions)

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is {part1()} (5067 is correct)')
    readFile('input.txt')
    print(f'part2 is {part2()} (1793 is correct)')
