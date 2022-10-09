n, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    interval = t[i] - t[i - 1]
    if interval > T:
        ans += T
    else:
        ans += interval

ans+=T
print(ans)
