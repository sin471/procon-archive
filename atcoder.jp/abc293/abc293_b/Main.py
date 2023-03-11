n = int(input())
a = list(map(int, input().split()))

called = [0] * n

for i in range(n):
    if called[i]:
        continue

    called[a[i] - 1] = 1

k = n - sum(called)
print(k)
print(*[i + 1 for i in range(n) if not called[i]])
