
numbers = []

def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        numbers.append(line.split())

def part1():
    list1 = []
    list2 = []
    for number in numbers:
        list1.append(number[0])
        list2.append(number[1])
    list1.sort()
    list2.sort()
    som = 0
    for i in range(len(list1)):
        verschil = abs(int(list1[i]) - int(list2[i]))
        som = som + verschil
    return som

def part2():
    list1 = []
    list2 = []
    for number in numbers:
        list1.append(number[0])
        list2.append(number[1])
    sum = 0
    for l1 in list1:
        sum += list2.count(l1) * int(l1)
    return sum

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is {part1()}')
    print(f'part2 is {part2()}')

