from bisect import bisect_left

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()

sb = [0] * (m + 1)
for j in range(m):
    sb[j + 1] = sb[j] + b[j]


ans = 0
for a_i in a:
    lessp = bisect_left(b, p - a_i)
    ans += sb[lessp] + a_i * lessp + p * (m - lessp)

print(ans)
