n, m = map(int, input().split())

k = []
a = []
for i in range(n):
    k_, *a_ = map(int, input().split())
    k.append(k_)
    a.append(a_)

counts = [0]*m

for i in a:
    for j in i:
        counts[j-1] += 1

ans = 0
for i in counts:
    if i == n:
        ans += 1

print(ans)
