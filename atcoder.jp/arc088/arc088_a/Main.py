from math import log2
x, y = map(int, input().split())

print(len(bin(y//x))-2)
