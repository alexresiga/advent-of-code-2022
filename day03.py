from string import ascii_letters as a

d = [x.strip() for x in open('data.in').readlines()]
print(sum(a.index(set.intersection(*map(set, [line[:len(line) // 2], line[len(line) // 2:]])).pop()) + 1 for line in d))
print(sum(a.index(set.intersection(*map(set, c)).pop()) + 1 for c in [d[k:k + 3] for k in range(0, len(d), 3)]))
