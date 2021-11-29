from itertools import groupby
from math import factorial
n = int(input())
s = input()
ans = 0


def comb(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))


for i, j in groupby(s):
    x = len(list(j))
    if x >= 2:
        ans += comb(x, 2)

print(ans)
