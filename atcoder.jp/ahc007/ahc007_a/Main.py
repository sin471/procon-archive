import sys
sys.setrecursionlimit(10**6)

n = 400
m = 1995

xy = [list(map(int, input().split())) for _ in range(n)]

uv = [list(map(int, input().split())) for _ in range(m)]


def dfs(graph, v):
    global seen
    seen[v] = 1
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(graph, next_v)


graph = [[] for _ in range(n)]


ans = 1

for u, v in uv:
    seen = [0]*n
    graph[u].append(v)
    graph[v].append(u)
    dfs(graph, u)

    print(ans, flush=True)
    if sum(seen) == n:
        ans = 0

# print(graph)
