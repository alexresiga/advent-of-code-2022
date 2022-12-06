d = open('data.in').read()
print('\n'.join(next(str(i) for i in range(size, len(d)) if len(set(d[i - size:i])) == size) for size in [4, 14]))
