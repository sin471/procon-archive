from functools import reduce

mod = 10**9 + 7
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

print(reduce(lambda x, y: (x * y) % mod, map(sum, a)))
