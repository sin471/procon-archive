import sys
import pypyjit
sys.setrecursionlimit(10**6)
pypyjit.set_param("max_unroll_recursion=0")

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1

    graph[a].append((b, x, y))
    graph[b].append((a, -x, -y))

pos = [None] * n


def dfs(i, nx, ny):
    if pos[i] is not None:
        return

    pos[i] = (nx, ny)
    for v, dx, dy in graph[i]:
        dfs(v, nx + dx, ny + dy)


dfs(0, 0, 0)
for i in pos:
    if i is None:
        print("undecidable")
    else:
        print(*i)
