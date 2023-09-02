l, r = map(int, input().split())


def sum_(a, b):
    n = b - a + 1
    return n * (a + b) // 2


ans = 0
mod = 10**9 + 7
for length in range(len(str(l)), len(str(r)) + 1):
    s = sum_(max(l, 10 ** (length - 1)), min(10 ** (length) - 1, r)) % mod
    ans += length * s % mod

print(ans % mod)
