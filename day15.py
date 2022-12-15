from re import findall

dist = lambda a, b, c, d: abs(a - c) + abs(b - d)
n = map(int, findall(r'-?\d+', open('data.in').read()))
sensors = [(b, a, dist(b, a, d, c), (d, c)) for a, b, c, d in zip(n, n, n, n)]
beacons = set(map(lambda b: b[3], sensors))
max_r, min_y, max_y = max(s[2] for s in sensors), min(map(lambda s: s[1], sensors)), max(map(lambda s: s[1], sensors))
N, M = 2000000, 4000000
part1 = 0
for j in range(-abs(min_y + max_r), max_y + max_r + 1):
    for ii, jj, radius, _ in sensors:
        if dist(N, j, ii, jj) <= radius and (N, j) not in beacons:
            part1 += 1
            break
print(part1)
for i, j, radius, _ in sensors:
    for k in range(radius + 1):
        for a in [-1, 1]:
            for b in [-1, 1]:
                x = i + a * k
                y = j + b * (radius + 1 - k)
                if 0 <= x <= M and 0 <= y <= M and all(dist(x, y, s[0], s[1]) > s[2] for s in sensors):
                    print(y * M + x)
                    exit()
