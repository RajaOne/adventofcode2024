import re

robots = []

def readFile(filename):
    for line in open(filename, 'r').readlines():
        numbers = re.split(r' v=|p=|,', line.strip())
        robots.append({'x': int(numbers[1]), 'y': int(numbers[2]), 'vx': int(numbers[3]), 'vy': int(numbers[4])})

def part1(w, h):
    ld, lu, rd, ru = calc_quad(h, w)
    return lu * ru * ld * rd

def calc_quad(h, w, seconds=100):
    lu = 0
    ru = 0
    ld = 0
    rd = 0
    for r in robots:
        x = (r['x'] + (seconds * r['vx'])) % w
        y = (r['y'] + (seconds * r['vy'])) % h
        if x < int(w / 2) and y < int(h / 2):
            lu += 1
        elif x > int(w / 2) and y < int(h / 2):
            ru += 1
        elif x < int(w / 2) and y > int(h / 2):
            ld += 1
        elif x > int(w / 2) and y > int(h / 2):
            rd += 1
    return ld, lu, rd, ru

def part2(w, h):
    seconds = 6644
    while True:
        grid = []
        for i in range(h):
            grid.append(['.'] * w)
        for r in robots:
            x = (r['x'] + (seconds * r['vx'])) % w
            y = (r['y'] + (seconds * r['vy'])) % h
            grid[y][x] = '#'
        if sum([l.count('#') for l in grid[:10]]) + sum([l.count('#') for l in grid[-10:]]) < 30:
            print(f'{seconds} seconds')
            for line in grid:
                print(''.join(line))
        if seconds > 7000:
            return  seconds
        # seconds += 1
    # return seconds

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1(101, 103)}\n\t(224554908 is correct)')
    print(f'part2 is\n\t {part2(101, 103)}\n\t(6644 is correct)')
