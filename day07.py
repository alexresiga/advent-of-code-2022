from collections import defaultdict
from itertools import accumulate

commands = [x.strip() for x in open('data.in').readlines()]
file_system = defaultdict(int)
cwd = []
for line in commands:
    match line.split():
        case '$', 'cd', '/':
            cwd = ['/']
        case '$', 'cd', '..':
            cwd.pop()
        case '$', 'cd', name:
            cwd.append(name + '/')
        case '$', 'ls':
            pass
        case 'dir', _:
            pass
        case size, _:
            for p in accumulate(cwd):
                file_system[p] += int(size)

print(sum(x for x in file_system.values() if x <= 100_000))
print(min(x for x in file_system.values() if x >= file_system['/'] - 40_000_000))
