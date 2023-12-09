import sys

import pypyjit

pypyjit.set_param("max_unroll_recursion=0")

sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
p = list(map(lambda x: int(x) - 1, input().split()))

graph = [[] * n for _ in range(n)]

for i in range(n - 1):
    graph[p[i]].append(i + 1)

b = [0] * n


def dfs(v, d):
    for u in graph[v]:
        dfs(u, d + 1)

    b[d] += a[v]


dfs(0, 0)
res = 0
for i in b[::-1]:
    if i != 0:
        res = i
        break

if res > 0:
    print("+")
elif res < 0:
    print("-")
else:
    if a[0] == 0:
        print(0)
    elif a[0] > 0:
        print("+")
    else:
        print("-")

# for _ in range(100000):
#     for i in range(n - 1):
#         a[p[i]] = a[p[i]] + a[i + 1]
# print(a)
