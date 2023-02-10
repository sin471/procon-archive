n, k = map(int, input().split())
mod = 10**9 + 7


def f(a, expponent):
    if a < 0 or expponent < 0:
        return 1

    result = 1
    while expponent:
        if expponent & 1:
            result *= a
            result %= mod
        expponent >>= 1
        a **= 2
        a %= mod

    return result
if n==1:
    print(k)
    exit()

ans = (((k * (k - 1)) % mod) * f(k - 2, n - 2)) % mod
print(ans)
