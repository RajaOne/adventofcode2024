import re

line = ""

def readFile(filename):
    global line
    line = open(filename, 'r').readlines()[0]

def part1():
    res = re.findall(r'mul\((\d+,\d+)\)', line)
    muls = [r.split(',') for r in res]
    return sum([(int(mul[0]) * int(mul[1])) for mul in muls])

def part2():
    total = 0
    dos = line.split('do()')
    for do in dos:
        donts = do.split("don't()")
        res = re.findall(r'mul\((\d+,\d+)\)', donts[0])
        muls = [r.split(',') for r in res]
        total += sum([(int(mul[0]) * int(mul[1])) for mul in muls])
    return total

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is {part1()} (170807108 is correct)')
    print(f'part2 is {part2()} (74838033 is correct)')
