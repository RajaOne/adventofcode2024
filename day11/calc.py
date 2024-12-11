numbers = []

def readFile(filename):
    for line in open(filename, 'r').read().split():
        numbers.append(int(line))

def part1():
    old_numbers = [n for n in numbers]
    for i in range(0, 25):
        new_numbers = []
        for number in old_numbers:
            if number == 0:
                new_numbers.append(1)
            elif len(str(number)) % 2 == 0:
                div = len(str(number)) // 2
                new_numbers.append(int(str(number)[:div]))
                new_numbers.append(int(str(number)[div:]))
            else:
                new_numbers.append(number * 2024)
        old_numbers.clear()
        [old_numbers.append(n) for n in new_numbers]
    return len(old_numbers)

def part2():
    total = 0

    knows = {}
    roots = [n for n in numbers]
    queue = []
    for number in roots:
        node = {'lvl': 0, 'number': number, 'next': [], 'ref': None}
        queue.append(node)

    counter = 0
    while len(queue) > 0 and counter < 600000:
        counter += 1
        node = queue.pop(0)
        if node['lvl'] > 75:
            continue
        if node['number'] in knows:
            node['ref'] = knows.get(node['number'])
            continue
        knows[node['number']] = node
        if node['number'] == 0:
            node['next'].append(1)
            queue.append({'lvl': node['lvl'] + 1, 'number': 1, 'next': [], 'ref': None})
        elif len(str(node['number'])) % 2 == 0:
            div = len(str(node['number'])) // 2
            node['next'].append(int(str(node['number'])[:div]))
            node['next'].append(int(str(node['number'])[div:]))
            queue.append({'lvl': node['lvl'] + 1, 'number': int(str(node['number'])[:div]), 'next': [], 'ref': None})
            queue.append({'lvl': node['lvl'] + 1, 'number': int(str(node['number'])[div:]), 'next': [], 'ref': None})
        else:
            node['next'].append(node['number'] * 2024)
            queue.append({'lvl': node['lvl'] + 1, 'number': node['number'] * 2024, 'next': [], 'ref': None})
    # print(f'counter: {counter}')

    for key in knows:
        knows[key]['counter'] = 0
        knows[key]['next_counter'] = 0
    for r in roots:
        knows.get(r)['counter'] = 1

    for i in range(0, 75):
        for key in knows:
            if knows[key]['counter'] == 0:
                continue
            if knows[key]['ref']:
                knows[knows[key]['ref']]['next_counter'] += knows[key]['counter']
            else:
                for n in knows[key]['next']:
                    knows[n]['next_counter'] += knows[key]['counter']
        for key in knows:
            knows[key]['counter'] = knows[key]['next_counter']
            knows[key]['next_counter'] = 0

    for key in knows:
        total += knows[key]['counter']
    return total

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(199986 is correct)')
    print(f'part2 is\n\t {part2()}\n\t(236804088748754 is correct)')
