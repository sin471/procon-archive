from math import isqrt
n = int(input())
s = sorted(input())
ans = 0
for i in range(isqrt(10**n) + 1):
        sq = str(i**2)
        if sorted(sq + "0" * (n - len(sq))) == s:
            ans += 1

print(ans)
