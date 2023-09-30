n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

ok = 0
ng = l + 1


def is_ok(width):
    cnt = 0
    last = 0
    for i in range(n):
        if l - a[i] >= width and a[i] - last >= width:
            cnt += 1
            last = a[i]

    return cnt >= k


while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
