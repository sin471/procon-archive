import sys

sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))


def gcd(x, y):
    if y == 0:
        return x

    return gcd(y, x % y)


g = gcd(a[0], a[1])
for i in range(2, n):
    g = gcd(g, a[i])

print(g)
