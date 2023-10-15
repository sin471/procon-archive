n, t = input().split()
n = int(n)
s = [list(input()) for _ in range(n)]

a = []
for i in range(n):
    cnt = 0
    for sij in s[i]:
        if sij == t[cnt]:
            cnt += 1
            if cnt >= len(t):
                break
    a.append(cnt)

b = []
for i in range(n):
    cnt = 0
    for sij in s[i][::-1]:
        if sij == t[-(cnt + 1)]:
            cnt += 1
            if cnt >= len(t):
                break
    b.append(cnt)

b.sort()
ans = 0
for ai in a:
    ok = len(b)
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if b[mid] >= (len(t) - ai):
            ok = mid
        else:
            ng = mid

    ans += len(b) - (ng + 1)

print(ans)
