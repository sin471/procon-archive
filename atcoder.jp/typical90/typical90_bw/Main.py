from math import ceil, log2, sqrt


def factorize(n):
    l = []
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i != 0:
            continue

        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        l.append((i, cnt))
    if n != 1:
        l.append((n, 1))

    return l


n = int(input())
primes = factorize(n)
s = sum(map(lambda x: x[1], primes))

print(ceil(log2(s)))
