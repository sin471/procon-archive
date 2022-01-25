n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]

h.sort()
l = []

ans=float("INF")
for i in range(k-1, n):
    diff=h[i]-h[i-k+1]
    ans=min(diff,ans)

print(ans)
