import sys

sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

colors = [-1] * n


def dfs(v, c):
    colors[v] = c
    for u in graph[v]:
        if colors[u] == -1:
            dfs(u, (c + 1) % 2)


dfs(0, 0)
b = []
h = []
for i in range(n):
    c = colors[i]
    if c == 0:
        b.append(i + 1)
    elif c == 1:
        h.append(i + 1)

l = b if len(b) >= len(h) else h

print(*l[: n // 2])
