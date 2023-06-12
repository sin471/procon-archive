from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

s = [0] * n

for i in range(1, n):
    if i % 2 == 0:
        s[i] = s[i - 1] + (a[i] - a[i - 1])
    else:
        s[i] = s[i - 1]

ans = 0
for l, r in lr:
    li = max(bisect_right(a, l) - 1, 0)
    ri = min(bisect_left(a, r), n - 1)
    ans = s[ri] - s[li]
    if li % 2 == 1:
        ans -= l - a[li]
    if ri % 2 == 0:
        ans -= a[ri] - r
    print(ans)
