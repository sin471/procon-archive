import sys

# import pypyjit

# pypyjit.set_param("max_unroll_recursion=0")
sys.setrecursionlimit(10**6)

n = int(input())
m = n - 1
ab = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = ab[i]
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(u):
    seen[u] = 1

    d = 0
    w = u
    for v in graph[u]:
        if seen[v]:
            continue

        d1, w1 = dfs(v)
        d1 += 1
        if d < d1:
            w = w1
            d = d1

    return (d, w)


seen = [0] * n
d, w = dfs(0)
seen = [0] * n
d, _ = dfs(w)

print(d + 1)
