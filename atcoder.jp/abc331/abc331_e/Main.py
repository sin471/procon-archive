n, m, l = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
cd = [set() for _ in range(n)]

for i in range(l):
    c, d = list(map(int, input().split()))
    cd[c - 1].add(d - 1)

s = sorted([(p, j) for j, p in enumerate(b)], reverse=True)

ans = float("-INF")
for i in range(n):
    j = 0
    for p, j in s:
        if j not in cd[i]:
            ans = max(ans, a[i] + p)
            break

print(ans)
