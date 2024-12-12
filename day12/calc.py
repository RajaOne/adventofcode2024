grid = []
clusters = []
covered = []
fields = {}

def readFile(filename):
    for line in open(filename, 'r').readlines():
        grid.append([n for n in line.strip()])

def part1():
    for row in grid:
        for field in row:
            if field not in fields:
                fields[field] = {'count': 0, 'fence': 0, 'score': 0}
    for row in grid:
        covered.append([False for n in row])

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if covered[y][x]:
                continue
            cluster = bfs(y, x)
            clusters.append(cluster)
            count = 0
            fence = 0
            for c_y, c_x in cluster['nodes']:
                to_add = 4
                if c_x-1>=0 and grid[c_y][c_x-1] == grid[c_y][c_x]:
                    to_add -= 2
                if c_y-1>=0 and grid[c_y-1][c_x] == grid[c_y][c_x]:
                    to_add -= 2
                count += 1
                fence += to_add
            fields[grid[y][x]]['score'] += count * fence
    return sum([fields[n]['score'] for n in fields])

def bfs(n_y, n_x):
    queue = [(n_y, n_x)]
    cluster = {'nodes': [], 'edges': []}
    while queue:
        y, x = queue.pop(0)
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]): continue
        if covered[y][x]: continue
        if grid[n_y][n_x] != grid[y][x]: continue
        cluster['nodes'].append((y, x))
        covered[y][x] = True
        queue.append((y+1, x))
        if (y, x) not in cluster['edges'] and (y-1<0 or grid[y-1][x] != grid[y][x]): cluster['edges'].append((y, x))
        else: queue.append((y-1, x))
        queue.append((y, x+1))
        queue.append((y, x-1))
    return cluster

def part2():
    return sum([len(cluster['nodes']) * count_sides(cluster) for cluster in clusters])

def count_sides(cluster):
    sides = 0
    while len(cluster['edges']) > 0:
        sides += count_sides2(cluster)
    return sides

def count_sides2(cluster):
    sides = 0
    start_y, start_x = cluster['edges'].pop(0)
    dir = 'right'
    y, x = start_y, start_x
    while True:
        if dir == 'right':
            if (y, x) in cluster['edges']: cluster['edges'].remove((y, x))
            if y - 1 >= 0 and x + 1 < len(grid[0]) and grid[y - 1][x + 1] == grid[y][x] and grid[y][x + 1] == grid[y][
                x]:
                dir = 'up'
                sides += 1
                y, x = y - 1, x + 1
            elif x + 1 >= len(grid[0]) or grid[y][x + 1] != grid[y][x]:
                dir = 'down'
                sides += 1
            else: y, x = y, x + 1
        elif dir == 'up':
            if y - 1 >= 0 and x - 1 >= 0 and grid[y - 1][x - 1] == grid[y][x] and grid[y - 1][x] == grid[y][x]:
                dir = 'left'
                sides += 1
                y, x = y - 1, x - 1
            elif y - 1 < 0 or grid[y - 1][x] != grid[y][x]:
                dir = 'right'
                sides += 1
            else: y, x = y - 1, x
        elif dir == 'left':
            if y + 1 < len(grid) and x - 1 >= 0 and grid[y + 1][x - 1] == grid[y][x] and grid[y][x - 1] == grid[y][x]:
                dir = 'down'
                sides += 1
                y, x = y + 1, x - 1
            elif x - 1 < 0 or grid[y][x - 1] != grid[y][x]:
                dir = 'up'
                sides += 1
            else: y, x = y, x - 1
        elif dir == 'down':
            if y+1<len(grid) and x+1<len(grid[0]) and grid[y+1][x+1] == grid[y][x] and grid[y+1][x] == grid[y][x]:
                dir = 'right'
                sides += 1
                y, x = y + 1, x + 1
            elif y + 1 >= len(grid) or grid[y + 1][x] != grid[y][x]:
                dir = 'left'
                sides += 1
            else: y, x = y + 1, x
        if y == start_y and x == start_x and dir == 'right':
            return sides

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is\n\t {part1()}\n\t(1473408 is correct)')
    print(f'part2 is\n\t {part2()}\n\t(886364 is correct)')
