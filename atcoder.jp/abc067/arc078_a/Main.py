n = int(input())
a = list(map(int, input().split()))


s = 0
sum_ = sum(a)
ans = float("INF")
for i in range(n - 1):
    s += a[i]
    x = s
    y = sum_ - s
    ans = min(ans, abs(x - y))

print(ans)
