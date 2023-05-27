n, m = map(int, input().split())

mod = 10**9 + 7


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        result %= mod
    return result


tmp = (factorial(max(n, m)) * factorial(min(n, m))) % mod
ans = 0
if abs(n - m) > 1:
    ans = 0
elif abs(n - m) == 1:
    ans = tmp
elif n == m:
    ans = (tmp * 2) % mod

print(ans)
