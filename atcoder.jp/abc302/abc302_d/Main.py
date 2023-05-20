n, m, d = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))


def is_ok(a_i, b_j):
    return b_j - a_i <= d
    
ans = -1
for a_i in a:
    ok = -1
    ng = m
    mid = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(a_i, b[mid]):
            ok = mid
        else:
            ng = mid
    

    if ok != -1 and a_i-b[ok]<=d:
        ans = max(ans, a_i + b[ok])

print(ans)
