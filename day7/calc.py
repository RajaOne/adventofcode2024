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

def check_test(test, total, numbers):
    if total > test:
        return False
    if len(numbers) == 1:
        return total + numbers[0] == test or total * numbers[0] == test
    return check_test(test, total + numbers[0], numbers[1:]) or check_test(test, total * numbers[0], numbers[1:])

def check_test2(test, total, numbers):
    if total > test:
        return False
    if len(numbers) == 0:
        return total == test
    return (check_test2(test, total + numbers[0], numbers[1:]) or
         check_test2(test, total * numbers[0], numbers[1:]) or
         check_test2(test, int(str(total) + str(numbers[0])), numbers[1:]))

def part1():
    return sum([equ['test'] for equ in equs if check_test(equ['test'], 0, equ['numbers'])])

def part2():
    return sum([equ['test'] for equ in equs if check_test2(equ['test'], equ['numbers'][0], equ['numbers'][1:])])

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(3598800864292 is correct)')
    print(f'part2 is\n\t {part2()}\n\t(340362529351427 is correct)')
