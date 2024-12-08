from httplib2.auth import token

grid = []
freqs = []

def readFile(filename):
    lines = open(filename, 'r').read().splitlines()
    [grid.append([c for c in line]) for line in lines]
    for line in grid:
        [freqs.append(c) for c in line if c not in freqs and c != '.']

def part1():
    negs = []
    for freq in freqs:
        found = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == freq:
                    found.append((x, y))
        for p in found:
            for p2 in found:
                if p == p2:
                    continue
                neg = (p[0] + (p[0] - p2[0]), p[1] + (p[1] - p2[1]))
                if neg not in negs:
                    negs.append(neg)
    total = 0
    for n in negs:
        if n[0] < 0 or n[0] >= len(grid[0]) or n[1] < 0 or n[1] >= len(grid):
            continue
        total += 1
    return total

def part2():
    return 0

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(... is correct)')
    print(f'part2 is\n\t {part2()}\n\t(... is correct)')
