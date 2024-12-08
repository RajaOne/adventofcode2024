equs = []

def readFile(filename):
    global equs
    lines = open(filename, 'r').read().splitlines()
    for line in lines:
        sections = line.split(': ')
        equ = {
            'test': int(sections[0]),
            'numbers': list(map(int, sections[1].split(' ')))
        }
        equs.append(equ)
    print(equs)

def check_test(test, total, numbers):
    if total > test:
        return False
    if len(numbers) == 1:
        return total + numbers[0] == test or total * numbers[0] == test
    return check_test(test, total + numbers[0], numbers[1:]) or check_test(test, total * numbers[0], numbers[1:])


def part1():
    total = 0
    for equ in equs:
        if check_test(equ['test'], 0, equ['numbers']):
            total += equ['test']
    return total

def part2():
    return 0

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is {part1()} (3598800864292 is correct)')
    print(f'part2 is {part2()} (... is correct)')
