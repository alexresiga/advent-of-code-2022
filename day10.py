from itertools import accumulate

values = [1] + [int(a) if a[-1].isdigit() else 0 for a in open('data.in').read().split()]
part1, part2 = {}, '\n'
for i, x in enumerate(accumulate(values), start=1):
    part1[i] = i * x
    part2 += '█' if (i - 1) % 40 - x in [-1, 0, 1] else ' '
    if not i % 40:
        part2 += '\n'
print(sum(part1[index] for index in range(20, 221, 40)), *part2)
