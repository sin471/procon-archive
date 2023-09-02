n, d, p = map(int, input().split())
f = list(map(int, input().split()))

f.sort(reverse=True)

ans = 0
l = 0

while l < n:
    s = sum(f[l : l + d])
    if s > p:
        ans += p
    else:
        ans += s
    l += d

print(ans)
