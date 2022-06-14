x, a, d, n = map(int, input().split())


def s(n):
    return a + (n - 1) * d


s_n = s(n)
if d < 0:
    a, s_n = s_n, a
    d *= -1

if x <= a and d > 0:
    ans = abs(a - x)
elif x >= s_n and d > 0:
    ans = abs(s_n - x)
else:

    ok = 0
    ng = n + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if s(mid) <= x:
            ok = mid
        else:
            ng = mid

    ans = min(abs(x - s(ok)), abs(x - s(ok + 1)))


print(ans)
