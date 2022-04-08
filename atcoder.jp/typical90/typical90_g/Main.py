n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a.sort()
INF = float("INF")


def bisect(b_i, a):
    ng = n
    ok = -1

    while abs(ng-ok) > 1:
        mid = (ng+ok)//2

        if a[mid] <= b_i:
            ok = mid
        else:
            ng = mid

    return ok


for b_i in b:
    ind = bisect(b_i, a)
    x, y = INF, INF
    if 0 <= ind < n:
        x = abs(a[ind]-b_i)

    if -1 <= ind < n-1:
        y = abs(a[ind+1]-b_i)

    print(min(x, y))
