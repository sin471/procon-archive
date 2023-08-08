from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ok = max(a[-1], b[-1]) + 2
ng = -1


def is_ok(x):
    can_sell = bisect_right(a, x)
    can_buy = m - bisect_left(b, x)
    return can_sell >= can_buy


while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
