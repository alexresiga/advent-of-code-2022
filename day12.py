def bfs(start):
    queue, seen = [[start]], {start}
    while queue:
        path = queue.pop(0)
        i, j = path[-1]
        if m[i][j] == "E":
            return path
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < len(m) and 0 <= y < len(m[0]) and f(m[x][y]) - f(m[i][j]) < 2 and (x, y) not in seen:
                queue.append(path + [(x, y)])
                seen.add((x, y))


m = [list(x.strip()) for x in open('data.in').readlines()]
f = lambda x: ord(x) if x not in 'SE' else ord('a') if x == 'S' else ord('z')
for part in ['S', 'aS']:
    starts = [(i, j) for j in range(len(m[0])) for i in range(len(m)) if m[i][j] in part]
    print(min(len(path) - 1 for s in starts if (path := bfs(s)) is not None))
