from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    d = bisect_left(a, i)
    print(a[d] - i)
