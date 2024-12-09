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
    numbers2 = []
    file_no = 0
    for n in range(0, len(numbers), 2):
        [numbers2.append(file_no) for _ in range(numbers[n])]
        if n+1 < len(numbers):
            [numbers2.append('.') for _ in range(numbers[n + 1])]
        file_no += 1
    file_no -= 1
    while file_no > 0:
        file_no_index = numbers2.index(file_no)
        space_needed = numbers2.count(file_no)
        index = find_free_space(numbers2, space_needed, file_no_index)
        if index == -1:
            file_no -= 1
            continue
        for i in range(space_needed):
            numbers2[index + i] = numbers2[file_no_index + i]
            numbers2[file_no_index + i] = '.'
        file_no -= 1
        while numbers2[-1] == '.': numbers2.pop()
    return sum([n * numbers2[n] for n in range(len(numbers2)) if numbers2[n] != '.'])

def find_free_space(list, space, max):
    count = 0
    for i in range(len(list)):
        if i >= max: return -1
        if list[i] == '.':
            count += 1
        else: count = 0
        if count == space:
            return i - space + 1
    return -1

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(6448989155953 is correct)')
    print(f'part2 is\n\t {part2()}\n\t(6476642796832 is correct)')
