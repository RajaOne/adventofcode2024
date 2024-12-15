import re

machines = []

def readFile(filename):
    for lines in open(filename, 'r').read().split('\n\n'):
        line = lines.split('\n')
        ax, ay = re.findall(r'(\d+)', line[0])
        bx, by = re.findall(r'(\d+)', line[1])
        dx, dy = re.findall(r'(\d+)', line[2])
        machines.append({'ax': int(ax), 'ay': int(ay), 'bx': int(bx), 'by': int(by), 'dx': int(dx), 'dy': int(dy)})

def check_node2(machine):
    b_incline = machine['by'] / machine['bx']
    a_incline = machine['ay'] / machine['ax']
    d_incline = machine['dy'] / machine['dx']

    if d_incline < a_incline and d_incline < b_incline: return 0
    if d_incline > a_incline and d_incline > b_incline: return 0

    switch = False
    if a_incline > d_incline:
        switch = True

    a_start = 0
    a_end = machine['dx']/machine['ax']
    while True:
        a_mid = int((a_end + a_start) / 2)
        calc_x = machine['ax'] * a_mid
        calc_y = machine['ay'] * a_mid
        calc_incline = (machine['dy'] - calc_y) / (machine['dx'] - calc_x)
        if a_start == a_mid:
            break
        if calc_incline == b_incline:
            break
        if (switch and calc_incline > b_incline) or (not switch and calc_incline < b_incline):
            a_start = a_mid
        if (switch and calc_incline < b_incline) or (not switch and calc_incline > b_incline):
            a_end = a_mid
    if calc_incline != b_incline: return 0
    b_mid = (machine['dx'] - calc_x) / machine['bx']
    if b_mid != int(b_mid): return 0
    return (3 * a_mid) + int(b_mid)

def part1():
    total = 0
    for machine in machines:
        total += check_node2(machine)
    return total

def part2():
    for m in machines:
        m['dx'] += 10000000000000
        m['dy'] += 10000000000000
    return part1()

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(33481 is correct)')
    print(f'part2 is\n\t {part2()}\n\t(92572057880885 is correct)')
