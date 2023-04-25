n, k, s = map(int, input().split())

x = s + 1 if s != 10**9 else 1

print(*([s] * k + (n - k) * [x]))
