from functools import cmp_to_key
from math import prod


def check(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else 1 if left > right else 0
    if isinstance(left, list) and isinstance(right, list):
        for res in map(check, left, right):
            if res:
                return res
        return check(len(left), len(right))
    if isinstance(left, int):
        return check([left], right)
    return check(left, [right])


packets = [[*map(eval, x.split())] for x in open('data.in').read().split('\n\n')]
print(sum(i for i, p in enumerate(packets, 1) if check(*p) == -1))
packets = sorted(sum(packets, [[2], [6]]), key=cmp_to_key(check))
print(prod(i for i, p in enumerate(packets, 1) if p in [[2], [6]]))
