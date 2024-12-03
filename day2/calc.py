grid = []

def readFile(filename):
    lines = open(filename, 'r').readlines()
    for line in lines:
        line = [int(i) for i in line.strip().split()]
        grid.append(line)

def part1():
    return sum([1 for line in grid if is_gradual(line)])

def is_gradual(line):
    num = line[0]
    is_inc = line[0] < line[1]
    for lineNum in line[1:]:
        if is_inc and num > lineNum:
            return 0
        if not is_inc and num < lineNum:
            return 0
        if 4 <= abs(num - lineNum) or abs(num - lineNum) <= 0:
            return 0
        num = lineNum
    return 1

def part2():
    return sum([1 for line in grid if is_gradual2(line)])

def is_gradual2(line):
    if is_gradual(line):
        return 1
    for i in range(len(line)):
        if is_gradual(line[:i] + line[i + 1:]):
            return 1
    return 0

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is {part1()} (402 is correct)')
    print(f'part2 is {part2()} (455 is correct)')
