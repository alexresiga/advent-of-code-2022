from parse import findall

data = list(findall('{:d}-{:d},{:d}-{:d}', open('data.in').read()))
print(sum(1 for a, b, c, d in data if a <= c <= d <= b or c <= a <= b <= d))
print(sum(1 for a, b, c, d in data if a <= d and c <= b))
