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

def check_node2(machine, x, y, actions, score):
    b_incline = machine['by'] / machine['bx']
    a_incline = machine['ay'] / machine['ax']
    d_incline = machine['dy'] / machine['dx']

    if d_incline < a_incline and d_incline < b_incline:
        return
    if d_incline > a_incline and d_incline > b_incline:
        return

    if a_incline <= d_incline:
        a_start = 0
        a_end = machine['dx']/machine['ax']

        a_mid = int((a_end + a_start) / 2)
        calc_x = machine['ax'] * a_mid
        calc_y = machine['ay'] * a_mid
        while a_start != a_mid:
            if (machine['dy'] - calc_y) / (machine['dx'] - calc_x) == b_incline:
                break
            if (machine['dy'] - calc_y) / (machine['dx'] - calc_x) < b_incline:
                a_start = a_mid
            if (machine['dy'] - calc_y) / (machine['dx'] - calc_x) > b_incline:
                a_end = a_mid
            a_mid = int((a_end + a_start) / 2)
            calc_x = machine['ax'] * a_mid
            calc_y = machine['ay'] * a_mid
        if (machine['dy'] - calc_y) / (machine['dx'] - calc_x) != b_incline:
            return
        score += 3 * a_mid
        if (machine['dx'] - calc_x)/machine['bx'] == int((machine['dx'] - calc_x)/machine['bx']):
            score += int((machine['dx'] - calc_x)/machine['bx'])
        else:
            return
        paths.append((actions, score))
    else :
        b_start = 0
        b_end = machine['dx']/machine['bx']

        b_mid = int((b_end + b_start) / 2)
        calc_x = machine['bx'] * b_mid
        calc_y = machine['by'] * b_mid
        while b_start != b_mid:
            if (machine['dy'] - calc_y) / (machine['dx'] - calc_x) == a_incline:
                break
            if (machine['dy'] - calc_y) / (machine['dx'] - calc_x) < a_incline:
                b_start = b_mid
            if (machine['dy'] - calc_y) / (machine['dx'] - calc_x) > a_incline:
                b_end = b_mid
            b_mid = int((b_end + b_start) / 2)
            calc_x = machine['bx'] * b_mid
            calc_y = machine['by'] * b_mid
        if (machine['dy'] - calc_y) / (machine['dx'] - calc_x) != a_incline:
            return
        score += 1 * b_mid
        if (machine['dx'] - calc_x)/machine['ax'] == int((machine['dx'] - calc_x)/machine['ax']):
            score += 3 * int((machine['dx'] - calc_x)/machine['ax'])
        else:
            return
        paths.append((actions, score))
    return

def part1():
    total = 0
    for machine in machines:
        paths.clear()
        check_node2(machine, 0, 0, [], 0)
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
    print(f'part2 is\n\t {part2()}\n\t(92572057880885 is correct)')
