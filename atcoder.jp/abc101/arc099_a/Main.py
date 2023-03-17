from math import ceil

n, k = map(int, input().split())
a = list(map(int, input().split()))

# ans*(k-1)+1>=n
print(ceil((n - 1) / (k - 1)))
