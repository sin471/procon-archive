from math import ceil, sqrt

n, m = map(int, input().split())

if n**2 < m:
    print(-1)
    exit()

# a<=bとすると、a<=sqrt(m)
ans = float("INF")
for a in range(1, ceil(sqrt(m + 1) + 1)):
    b = ceil(m / a)
    x = a * b
    if a <= n and b <= n and x >= m:
        ans = min(x, ans)

print(ans)
