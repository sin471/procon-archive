from typing import Counter


A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

coupons = [list(map(int, input().split())) for _ in range(M)]

ans = min(a)+min(b)

for x_i, y_i, c_i in coupons:
    s = a[x_i-1]+b[y_i-1]-c_i
    ans=min(ans,s)

print(ans)
