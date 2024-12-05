rules = []
updates = []

def readFile(filename):
    sections = open(filename, 'r').read().split('\n\n')
    [rules.append(list(map(int, rule.split('|')))) for rule in sections[0].splitlines()]
    [updates.append(list(map(int, update.split(',')))) for update in sections[1].splitlines()]

def part1():
    return sum([update[int(len(update)/2)] for update in updates if rules_valid(update)])

def part2():
    total = 0
    incorrect_updates = [update for update in updates if not rules_valid(update)]
    for update in incorrect_updates:
        while not rules_valid(update):
            fix_rules(update)
        total += update[int(len(update)/2)]
    return total

def rules_valid(update):
    for rule in rules:
        found_second = False
        for num in update:
            if num == rule[1]: found_second = True
            if num == rule[0] and found_second: return False
    return True

def fix_rules(update):
    num_i = 0
    for rule in rules:
        found_second = False
        for i in range(len(update)):
            num = update[i]
            if num == rule[1]:
                found_second = True
                num_i = i
            if num == rule[0] and found_second:
                update[num_i], update[i] = update[i], update[num_i]

if __name__ == "__main__":
    readFile('input.txt')
    print(f'part1 is {part1()} (4462 is correct)')
    print(f'part2 is {part2()} (6767 is correct)')
