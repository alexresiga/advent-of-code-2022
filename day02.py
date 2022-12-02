lines = [x.strip().split(' ') for x in open('data.in').readlines()]
rps = dict(A=("Z", 1, "Y"), X=("C", 1, "B"), B=("X", 2, "Z"), Y=("A", 2, "C"), C=("Y", 3, "X"), Z=("B", 3, "A"))
print(sum(rps[u][1] if u == rps[t][0] else 6 + rps[u][1] if t == rps[u][0] else 3 + rps[u][1] for t, u in lines))
print(sum(rps[t][1] + 3 if u == 'Y' else rps[rps[t][0]][1] if u == 'X' else 6 + rps[rps[t][2]][1] for t, u in lines))
