from collections import defaultdict

grid = defaultdict(lambda: '.')
for line in [x.strip() for x in open('data.in').readlines()]:
    coords = list(map(lambda x: tuple(map(int, x.split(','))), line.split(' -> ')))
    for (a, b), (c, d) in zip(coords, coords[1:]):
        for i in range(min(a, c), max(a, c) + 1):
            for j in range(min(b, d), max(b, d) + 1):
                grid[(i, j)] = '#'


def move(x, y, part1=True):
    for ii, jj in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if grid[(ii, jj)] not in 'o#' and (part1 or jj != floor):
            return ii, jj
    return x, y


start_x, start_y = 500, 0
prev = (start_x, start_y)
floor = max(map(lambda x: x[1], grid.keys())) + 2
while True:
    # new = move(*prev) part 1
    new = move(*prev, False)
    if new == prev:
        grid[new] = 'o'
        prev = (start_x, start_y)
        if new == (500, 0):
            break
    else:
        if new[1] > floor:
            break
        prev = new

print(len(list(filter(lambda x: x == 'o', grid.values()))))
