import sys
from itertools import combinations

sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
uvw = []

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    uvw.append([u, v, w])


def root(x):
    if par[x] == x:
        return x

    r = root(par[x])
    par[x] = r
    return r


def unite(x, y):
    rx = root(x)
    ry = root(y)
    if size[rx] <= size[ry]:
        par[rx] = ry
        size[ry] += size[rx]
    else:
        par[ry] = rx
        size[rx] += size[ry]


def same(x, y):
    return root(x) == root(y)


ans = float("INF")

for edges in combinations(range(m), n - 1):
    par = list(range(n))
    size = [1] * n
    cost = 0
    for e in edges:
        u, v, w = uvw[e]
        if same(u, v):
            cost = k
            break
        else:
            cost = (cost + w) % k
            unite(u, v)

    ans = min(ans, cost)

print(ans)
