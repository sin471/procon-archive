from collections import Counter

n = int(input())
s = input()

c = Counter(s)
mod = 10**9 + 7
ans = 1
for i in c.values():
    ans *= i + 1
    ans %= mod

print(ans - 1)
