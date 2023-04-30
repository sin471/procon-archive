from itertools import accumulate
from math import floor, sqrt

n = int(input())
is_prime = [1] * (floor(sqrt(n)) + 1)
is_prime[0] = is_prime[1] = 0

primes = []
for p in range(2, len(is_prime)):
    if not is_prime[p]:
        continue
    primes.append(p)
    for x in range(p**2, len(is_prime), p):
        is_prime[x] = 0

s = list(accumulate(is_prime))
ans = 0

for i in range(len(primes)):
    a = primes[i]
    if a**5 > n:
        break
    for j in range(i + 1, len(primes)):
        b = primes[j]
        d = floor(sqrt(n // (a * a * b)))

        if d < b or b**3 > n:
            break
        ans += s[d] - s[b]

print(ans)
