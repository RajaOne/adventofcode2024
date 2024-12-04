grid = []

def readFile(filename):
    lines = open(filename, 'r').readlines()
    [grid.append(line.strip()) for line in lines]

def part1():
    total = 0
    for i, row in enumerate(grid):
        for j in range(0, len(row)-3):
            if row[j] + row[j + 1] + row[j + 2] + row[j + 3] in ("XMAS", "SAMX"): total += 1
    for i in range(len(grid[0])):
        for j in range(0, len(grid)-3):
            if grid[j][i] + grid[j + 1][i] + grid[j + 2][i] + grid[j + 3][i] in ("XMAS", "SAMX"): total += 1
    for i in range(0, len(grid)-3):
        for j in range(0, len(grid[i])-3):
            if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] + grid[i + 3][j + 3] in ("XMAS", "SAMX"): total += 1
    for i in range(0, len(grid)-3):
        for j in range(3, len(grid[i])):
            if grid[i][j] + grid[i + 1][j - 1] + grid[i + 2][j - 2] + grid[i + 3][j - 3] in ("XMAS", "SAMX"): total += 1
    return total

def part2():
    total = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            word1 = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
            word2 = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]
            if (word1 in ("MAS", "SAM")) and (word2 in ("MAS", "SAM")): total += 1
    return total

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is {part1()} (2524 is correct)')
    print(f'part2 is {part2()} (1873 is correct)')
