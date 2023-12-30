from math import ceil

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

a = [0] + a + [n + 1]
k = n
l = []
for i in range(len(a) - 1):
    x = a[i + 1] - a[i] - 1
    if x == 0:
        continue
    l.append(x)
    k = min(k, x)

ans = 0
for i in l:
    ans += ceil(i / k)

print(ans)
