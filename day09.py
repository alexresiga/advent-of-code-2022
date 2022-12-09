steps = [x.strip().split() for x in open('data.in').readlines()]

# rope = [[0, 0] for _ in range(2)]
rope = [[0, 0] for _ in range(10)]
dirs = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
res = {(0, 0)}
sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)  # thanks to /u/nthistle for this


def move(head, tail):
    global rope
    d_i = tail[0] - head[0]
    d_j = tail[1] - head[1]
    if d_i == 0 or d_j == 0:
        if abs(d_i) >= 2:
            tail[0] -= sign(d_i)
        if abs(d_j) >= 2:
            tail[1] -= sign(d_j)
    elif (abs(d_i), abs(d_j)) != (1, 1):
        tail[0] -= sign(d_i)
        tail[1] -= sign(d_j)


for direction, n in steps:
    for _ in range(int(n)):
        x, y = dirs[direction]
        rope[0][0] += x
        rope[0][1] += y
        for lead, follow in zip(rope, rope[1:]):
            move(lead, follow)
        res.add(tuple(rope[-1]))

print(len(res))
