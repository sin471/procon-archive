from math import factorial
n = int(input())
c = list(map(int, input().split()))

mod = 10**9+7

c.sort()

combination = 1

for i in range(n):
    a = c[i]-i
    if a <= 0:
        combination = 0
        break
    combination = combination*(c[i]-i) % mod

print(combination)
