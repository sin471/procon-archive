import sys

import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param("max_unroll_recursion=0")


n = int(input())

graph = [[] for _ in range(n)]

for i in range(n - 1):
    d_i = map(int, input().split())
    for j, d_ij in enumerate(d_i, i + 1):
        graph[i].append((j, d_ij))
        graph[j].append((i, d_ij))


def dfs():
    if all(used):
        return 0
    v = used.index(0)
    used[v] = 1
    res = -1
    for w, d in graph[v]:
        if used[w]:
            continue
        used[w] = 1
        res = max(res, dfs() + d)
        used[w] = 0
    used[v] = 0
    return res


ans = 0
used = [0] * n
if n % 2 == 0:
    ans = dfs()
else:
    for v in range(n):
        used[v] = 1
        ans = max(ans, dfs())
        used[v] = 0
        
print(ans)
