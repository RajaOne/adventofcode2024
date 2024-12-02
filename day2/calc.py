grid = []

def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = [int(i) for i in line.split()]
        grid.append(line)

def part1():
    sum = 0
    for line in grid:
        if is_gradual(line):
            sum += 1
    return sum

def is_gradual(line):
    num = line[0]
    is_inc = line[0] < line[1]
    for lineNum in line[1:]:
        if is_inc and num > lineNum:
            return 0
        elif not is_inc and num < lineNum:
            return 0
        if 4 <= abs(num - lineNum) or abs(num - lineNum) <= 0:
            return 0
        num = lineNum
    return 1

def part2():
    sum = 0
    for line in grid:
        if is_gradual2(line):
            sum += 1
    return sum

def is_gradual2(line):
    if is_gradual(line):
        return 1
    for i in range(len(line)):
        if is_gradual(line[:i] + line[i + 1:]):
            return 1
    return 0
    # below code does not work
    # num = line[0]
    # is_inc = line[0] < line[1]
    # for i in range(1, len(line)):
    #     lineNum = line[i]
    #     if is_inc and num > lineNum:
    #         return is_gradual(line[:i] + line[i + 1:]) or is_gradual(line[:i - 1] + line[i:])
    #     elif not is_inc and num < lineNum:
    #         return is_gradual(line[:i] + line[i + 1:]) or is_gradual(line[:i - 1] + line[i:])
    #     if 4 <= abs(num - lineNum) or abs(num - lineNum) <= 0:
    #         return is_gradual(line[:i] + line[i + 1:]) or is_gradual(line[:i - 1] + line[i:])
    #     num = lineNum
    # return 1

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is {part1()} (402 is correct)')
    print(f'part2 is {part2()} (455 is correct)')

