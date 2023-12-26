n, k = map(int, input().split())
a = list(map(int, input().split()))
s1 = [0] * (k + 1)
s2 = [0] * (k + 1)

for i in range(k):
    s1[i + 1] = s1[i]
    if i % 2 == 1:
        s1[i + 1] += a[i] - a[i - 1]

for i in range(k):
    i2 = k - i - 1
    s2[i2] = s2[i2 + 1]
    if i % 2 == 1:
        s2[i2] += a[i2 + 1] - a[i2]

ans = float("INF")

if k % 2 == 0:
    print(s1[-1])
    exit()

for i in range(k):
    if i % 2 == 0:
        ans = min(ans, s1[i] + s2[i + 1])
    else:
        ans = min(ans, s1[i - 1] + s2[i + 2] + a[i + 1] - a[i - 1])

print(ans)
