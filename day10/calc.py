grid = []
starts = []

def readFile(filename):
    for line in open(filename, 'r').read().splitlines():
        grid.append([int(x) for x in line])
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                starts.append((x, y))

def part1():
    total = 0
    for start in starts:
        ends = 0
        found = []
        queue = [(start[0], start[1], 0)]
        while queue:
            x, y, c = queue.pop(0)
            if (x, y) in found: continue
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid): continue
            if grid[y][x] != c: continue
            found.append((x, y))
            if grid[y][x] == 9 and c == 9:
                ends += 1
            queue.append((x+1, y, c+1))
            queue.append((x-1, y, c+1))
            queue.append((x, y+1, c+1))
            queue.append((x, y-1, c+1))
        total += ends
    return total

def part2():
    total = 0
    for start in starts:
        ends = 0
        queue = [(start[0], start[1], 0)]
        while queue:
            x, y, c = queue.pop(0)
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid): continue
            if grid[y][x] != c: continue
            if grid[y][x] == 9 and c == 9:
                ends += 1
            queue.append((x+1, y, c+1))
            queue.append((x-1, y, c+1))
            queue.append((x, y+1, c+1))
            queue.append((x, y-1, c+1))
        total += ends
    return total

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(841 is correct)')
    print(f'part2 is\n\t {part2()}\n\t(1875 is correct)')
