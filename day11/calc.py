numbers = []

def readFile(filename):
    for line in open(filename, 'r').read().split():
        numbers.append(int(line))

def part1():
    for i in range(0, 25):
        new_numbers = []
        for number in numbers:
            if number == 0:
                new_numbers.append(1)
            elif len(str(number)) % 2 == 0:
                div = len(str(number)) // 2
                new_numbers.append(int(str(number)[:div]))
                new_numbers.append(int(str(number)[div:]))
            else:
                new_numbers.append(number * 2024)
        numbers.clear()
        [numbers.append(n) for n in new_numbers]
    return len(numbers)

def part2():
    total = 0
    return total

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(. is correct)')
    print(f'part2 is\n\t {part2()}\n\t(. is correct)')
