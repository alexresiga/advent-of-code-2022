data = [x.strip() for x in open('data.in').readlines()]
part1, part2 = 99 + 98 + 98 + 97, 0
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(1, len(data) - 1):
    for j in range(1, len(data) - 1):
        for d in dirs:
            x, y = i + d[0], j + d[1]
            while 0 < x < len(data) - 1 and 0 < y < len(data) - 1 and data[i][j] > data[x][y]:
                x, y = x + d[0], y + d[1]
            if data[i][j] > data[x][y] and (x == 0 or x == len(data) - 1 or y == 0 or y == len(data) - 1):
                part1 += 1
                break
print(part1)
for i in range(1, len(data) - 1):
    for j in range(1, len(data) - 1):
        score = 1
        for d in dirs:
            count = 0
            x, y = i + d[0], j + d[1]
            while 0 <= x <= len(data) - 1 and 0 <= y <= len(data) - 1:
                count += 1
                if data[i][j] <= data[x][y]:
                    break
                x, y = x + d[0], y + d[1]
            score *= count
        part2 = max(part2, score)
print(part2)
