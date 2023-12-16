import sys

# import pypyjit
# pypyjit.set_param("max_unroll_recursion=0")
sys.setrecursionlimit(10**6)


n = int(input())
g = [[] * n for _ in range(n)]
visited = [0] * n
for i in range(n - 1):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


def dfs(v):
    visited[v] = 1
    if len(g[v]) == 1:
        return 1
    res = 0
    for u in g[v]:
        if not visited[u]:
            res += dfs(u)
    return res + 1


l = []
visited[0] = 1
for v in g[0]:
    res = dfs(v)
    l.append(res)

print(sum(l) - max(l) + 1)
