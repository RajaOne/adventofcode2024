
numbers = []

def readFile(filename):
    lines = open(filename, 'r').readlines()
    [numbers.append(line.strip().split()) for line in lines]

def part1():
    list1 = [number[0] for number in numbers]
    list2 = [number[1] for number in numbers]
    list1.sort()
    list2.sort()
    return sum([abs(int(list1[i]) - int(list2[i])) for i in range(len(list1))])

def part2():
    list1 = [number[0] for number in numbers]
    list2 = [number[1] for number in numbers]
    return sum([int(l1) * list2.count(l1) for l1 in list1])

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is {part1()} (1189304 is correct)')
    print(f'part2 is {part2()} (24349736 is correct)')
