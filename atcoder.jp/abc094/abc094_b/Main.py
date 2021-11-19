import bisect
n, m, x = map(int, input().split())

a = list(map(int, input().split()))

xi = bisect.bisect(a, x)
a_0 = len(a[0:xi])
a_n = len(a)-a_0
print(a_0 if a_0 <= a_n else a_n)
