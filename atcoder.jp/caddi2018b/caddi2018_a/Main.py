from math import ceil

n, p = map(int, input().split())

primes = dict()

for i in range(2, ceil(p**0.5) + 1):
    while p % i == 0:
        p //= i
        primes.setdefault(i, 0)
        primes[i] += 1
if p != 1:
    primes[p] = 1
ans = 1
for prime, k in primes.items():
    if k // n > 0:
        ans *= prime ** (k // n)

print(ans)
