numbers = []

def readFile(filename):
    for line in open(filename, 'r').read().splitlines():
        [numbers.append(int(c)) for c in line]

def part1():
    numbers2 = []
    file_no = 0
    for n in range(0, len(numbers), 2):
        [numbers2.append(file_no) for _ in range(numbers[n])]
        if n+1 < len(numbers):
            [numbers2.append('.') for _ in range(numbers[n + 1])]
        file_no += 1

    while numbers2.count('.') > 0:
        numbers2[numbers2.index('.')] = numbers2.pop()
        while numbers2[-1] == '.': numbers2.pop()

    return sum([n * numbers2[n] for n in range(len(numbers2))])

def part2():
    return 0

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(6448989155953 is correct)')
    print(f'part2 is\n\t {part2()}\n\t(... is correct)')
