data = sorted([sum(map(int, x.split('\n'))) for x in open('data.in').read().split('\n\n')])
print(data[-1], sum(data[-3:]))
