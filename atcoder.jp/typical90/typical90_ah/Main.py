from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(int)
m = 0
j = 0
ans = 0

for i in range(n):
    if j < i:
        j = i
    while j < n and (m < k or d[a[j]] > 0):
        if d[a[j]] == 0:
            m += 1

        d[a[j]] += 1
        j += 1

    ans = max(ans, j - i)

    d[a[i]] -= 1
    if d[a[i]] == 0:
        m -= 1


print(ans)
