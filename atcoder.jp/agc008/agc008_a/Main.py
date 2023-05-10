x, y = map(int, input().split())
ans = float("INF")
if y >= x:
    ans = min(ans, y - x)
if y >= -x:
    ans = min(ans, y + x + 1)
if -y >= x:
    ans = min(ans, -(y + x) + 1)
if -y >= -x:
    ans = min(ans, -y + x + 2)

print(ans)
