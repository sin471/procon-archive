from math import ceil

n = int(input())
a = list(map(int, input().split()))

s = sum(a)

# n*(h-1)<s<=n*h
# ならしたときの最大の高さh

h = s // n if s % n == 0 else s // n + 1

p = 0
m = 0
for i in range(n):
    if a[i] < h - 1:
        p += (h - 1) - a[i]
    if a[i] > h:
        m += a[i] - h 

print(max(p, m))
