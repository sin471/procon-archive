n = int(input())
a = list(map(int, input().split()))

p = [0] * (n + 1)

mod = 998244353


def mod_inv(n, m, mod):
    res = 1
    a = n
    while m:
        if m & 1:
            res *= a
            res %= mod

        a **= 2
        a %= mod
        m = m >> 1

    return res


invn = mod_inv(n, mod - 2, mod)

p[0] = 1
p[1]=invn
for i in range(2, n + 1):
    p[i] = p[i - 1] + p[i - 1] * invn
    p[i] %= mod

ans = 0
for i in range(n):
    ans += a[i] * p[i + 1]
    ans %= mod


print(ans)
