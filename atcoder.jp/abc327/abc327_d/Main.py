import sys

import pypyjit

pypyjit.set_param("max_unroll_recursion=0")
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for ai, bi in zip(a, b):
    graph[ai - 1].append(bi - 1)
    graph[bi - 1].append(ai - 1)


colors = [-1] * n


def dfs(color, v):
    colors[v] = color
    res = True

    for u in graph[v]:
        if colors[u] == color:
            return False

        if colors[u] != -1:
            continue

        res = res and dfs(not color, u)
    return res


ans = True
for i in range(n):
    if colors[i] == -1:
        ans = ans and dfs(0, i)

print("Yes" if ans else "No")
