from bisect import bisect_left

n = int(input())
l = list(map(int, input().split()))
l.sort()

"""
a-b<c
b-a<c
abs(a-b)<c<a+b
"""

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        a, b = l[i], l[j]
        k = bisect_left(l, a + b)
        ans += k - j - 1


print(ans)
