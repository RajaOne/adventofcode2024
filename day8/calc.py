grid = []
freqs = []

def readFile(filename):
    lines = open(filename, 'r').read().splitlines()
    [grid.append([c for c in line]) for line in lines]
    for line in grid:
        [freqs.append(c) for c in line if c not in freqs and c != '.']

def part1():
    negs = {}
    for freq in freqs:
        found = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == freq:
                    found.append((x, y))
        for p in found:
            for p2 in found:
                if p == p2: continue
                neg = (p[0] + (p[0] - p2[0]), p[1] + (p[1] - p2[1]))
                negs[neg] = 1
    return sum([1 for n in negs if not outside_grid(n)])

def part2():
    negs = []
    neg_grid = []
    for line in grid:
        neg_grid.append([c for c in line])
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
                dist = (p[0] - p2[0], p[1] - p2[1])
                neg = (p[0] + (dist[0]), p[1] + (dist[1]))
                while not outside_grid(neg):
                    if neg not in negs:
                        negs.append(neg)
                        neg_grid[neg[1]][neg[0]] = '#'
                    neg = (neg[0] + dist[0], neg[1] + dist[1])
    total = 0
    for line in neg_grid:
        total += sum([1 for c in line if c != '.'])
    return total

def outside_grid(n):
    return n[0] < 0 or n[0] >= len(grid[0]) or n[1] < 0 or n[1] >= len(grid)

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(354 is correct)')
    print(f'part2 is\n\t {part2()}\n\t(1263 is correct)')
