n, X = map(int, input().split())
x = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


g = 0
for i in range(n):
    g = gcd(g, abs(X - x[i]))

print(g)
