from math import ceil
a, b = map(int, input().split())
n = 0

n = ceil((b-1)/(a-1))
print(n)
