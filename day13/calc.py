import re

machines = []

def readFile(filename):
    for lines in open(filename, 'r').read().split('\n\n'):
        line = lines.split('\n')
        ax, ay = re.findall(r'(\d+)', line[0])
        bx, by = re.findall(r'(\d+)', line[1])
        dx, dy = re.findall(r'(\d+)', line[2])
        machines.append({'ax': int(ax), 'ay': int(ay), 'bx': int(bx), 'by': int(by), 'dx': int(dx), 'dy': int(dy)})

paths = []

def check_node(machine, x, y, actions, score):
    b_incline = machine['by'] / machine['bx']
    while (machine['dy'] - y)/(machine['dx'] - x) != b_incline:
        x += machine['ax']
        y += machine['ay']
        score += 3
        if x >= machine['dx'] or y >= machine['dy']:
            return
    print("starting second loop")
    while not (x == machine['dx'] and y == machine['dy']):
        x += machine['bx']
        y += machine['by']
        score += 1
        if x > machine['dx'] or y > machine['dy']:
            return
    paths.append((actions, score))

def part1():
    total = 0
    for machine in machines:
        paths.clear()
        check_node(machine, 0, 0, [], 0)
        if len(paths) > 0:
            total += paths[0][1]
    return total

def part2():
    for m in machines:
        m['dx'] += 10000000000000
        m['dy'] += 10000000000000
    return part1()

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(33481 is correct)')
    # print(f'part2 is\n\t {part2()}\n\t(... is correct)')
