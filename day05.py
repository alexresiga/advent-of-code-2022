from parse import findall
from collections import defaultdict

arr, steps = [x for x in open('data.in').read().split('\n\n')]
lines = [x.replace('    ', '0 ').split(' ') for x in arr.split('\n')]
stacks, steps = defaultdict(list), list(findall('move {:d} from {:d} to {:d}', steps))

for line in reversed(lines[:-1]):
    for i, elem in enumerate(line, start=1):
        if elem != '0' and elem != '':
            stacks[i].append(elem)
for amount, source, dest in steps:
    stacks[source], stacks[dest] = stacks[source][:-amount], stacks[dest] + list(reversed(stacks[source][-amount:]))
    # stacks[source], stacks[dest] = stacks[source][:-amount], stacks[dest] + stacks[source][-amount:] part 2

print(''.join([x[1][-1] for x in sorted(stacks.items())]).replace('][', ''))
