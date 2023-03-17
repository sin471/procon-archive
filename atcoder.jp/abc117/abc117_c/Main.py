n, m = map(int, input().split())
x = sorted(map(int, input().split()))

if n >= m:
    print(0)
    exit()

l = []
for i in range(m - 1):
    l.append(x[i + 1] - x[i])

l.sort(reverse=True)
del l[: n - 1]
print(sum(l))
