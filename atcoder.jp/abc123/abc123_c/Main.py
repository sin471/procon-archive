from math import ceil

n = int(input())
x = [int(input()) for _ in range(5)]

print(4 + ceil(n / min(x)))
