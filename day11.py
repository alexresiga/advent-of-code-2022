import math
import re
from collections import defaultdict
from copy import deepcopy

ints = lambda text: list(map(int, re.findall(r'\d+', text)))
operation = lambda old, sign, val: old + int(val) if sign == '+' else old * int(val) if val.isdigit() else old * old
monkeys = {}
for i, monkey in enumerate([x.strip() for x in open('data.in').read().split('\n\n')]):
    line = [x.strip() for x in monkey.split('\n')]
    items = ints(line[1])
    op = line[2].split()[-2:]
    test, true, false = map(lambda x: ints(x)[0], line[3:6])
    monkeys[i] = [items, op, test, true, false]
modulo = math.prod(map(lambda x: x[2], monkeys.values()))
for part in [20, 10_000]:
    arctic_monkeys = deepcopy(monkeys)
    inspections = defaultdict(int)
    for t in range(part):
        for i in arctic_monkeys.keys():
            inspections[i] += len(arctic_monkeys[i][0])
            while len(arctic_monkeys[i][0]) > 0:
                item = arctic_monkeys[i][0].pop(0)
                new = operation(item, *arctic_monkeys[i][1])
                new = new // 3 % modulo if part == 20 else new % modulo
                dest = arctic_monkeys[i][3] if new % arctic_monkeys[i][2] == 0 else arctic_monkeys[i][4]
                arctic_monkeys[dest][0].append(new)
    print(math.prod(sorted(inspections.values())[-2:]))
