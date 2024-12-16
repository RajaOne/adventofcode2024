grid = []
movements = []

def readFile(filename):
    grid.clear()
    movements.clear()
    segments = open(filename, 'r').read().split('\n\n')
    for lines in segments[0].strip().split():
        grid.append([n for n in lines])
    for m in segments[1].strip():
        movements.append(m)

def move_up(start):
    new_x, new_y = (start[0], start[1] - 1)
    i_x, i_y = (start[0], start[1] - 1)
    while i_y > 0 and grid[i_y][i_x] == 'O':
        i_y -= 1
    if grid[i_y][i_x] == '.':
        while i_y != start[1]:
            grid[i_y][i_x] = 'O'
            i_y += 1
        grid[new_y][new_x] = '@'
        grid[start[1]][start[0]] = '.'
        return new_x, new_y
    else:
        return start


def move_right(start):
    new_x, new_y = (start[0] + 1, start[1])
    i_x, i_y = (start[0] + 1, start[1])
    while i_x < len(grid[i_y]) and grid[i_y][i_x] == 'O':
        i_x += 1
    if grid[i_y][i_x] == '.':
        while i_x != start[0]:
            grid[i_y][i_x] = 'O'
            i_x -= 1
        grid[new_y][new_x] = '@'
        grid[start[1]][start[0]] = '.'
        return new_x, new_y
    else:
        return start


def move_down(start):
    new_x, new_y = (start[0], start[1] + 1)
    i_x, i_y = (start[0], start[1] + 1)
    while i_y < len(grid) and grid[i_y][i_x] == 'O':
        i_y += 1
    if grid[i_y][i_x] == '.':
        while i_y != start[1]:
            grid[i_y][i_x] = 'O'
            i_y -= 1
        grid[new_y][new_x] = '@'
        grid[start[1]][start[0]] = '.'
        return new_x, new_y
    else:
        return start


def move_left(start):
    new_x, new_y = (start[0] - 1, start[1])
    i_x, i_y = (start[0] - 1, start[1])
    while i_x > 0 and grid[i_y][i_x] == 'O':
        i_x -= 1
    if grid[i_y][i_x] == '.':
        while i_x != start[0]:
            grid[i_y][i_x] = 'O'
            i_x += 1
        grid[new_y][new_x] = '@'
        grid[start[1]][start[0]] = '.'
        return new_x, new_y
    else:
        return start


def part1():
    start = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                start = (x, y)
    for m in movements:
        # print(m)
        if m == '^':
            start = move_up(start)
        if m == '>':
            start = move_right(start)
        if m == 'v':
            start = move_down(start)
        if m == '<':
            start = move_left(start)
#         for y in grid: print(''.join(y))
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'O':
                total += ((y*100) + x)

    return total

def part2():
    return 0

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(.. is correct)')
    print(f'part2 is\n\t {part2()}\n\t(.. is correct)')
