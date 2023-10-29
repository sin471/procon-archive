from bisect import bisect_right

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    j = bisect_right(a, a[i] + m - 1)
    ans = max(j - i, ans)

print(ans)
