from collections import defaultdict
n, q = map(int, input().split())
a = list(map(int, input().split()))
xk = [list(map(int, input().split())) for _ in range(q)]


d = defaultdict(list)

for i, ai in enumerate(a, 1):
    d[ai].append(i)

for x, k in xk:
    if k <= len(d[x]):
        print(d[x][k-1])
    else:
        print(-1)
