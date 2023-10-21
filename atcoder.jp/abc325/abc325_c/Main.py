import sys

import pypyjit
pypyjit.set_param("max_unroll_recursion=0")
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

d = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
seen = [[0] * w for i in range(h)]


def is_inside(x, y, h, w):
    return 0 <= x < h and 0 <= y < w


def dfs(i, j):
    if not is_inside(i, j, h, w) or seen[i][j] or s[i][j] == ".":
        return
    seen[i][j] = 1
    for di, dj in d:
        dfs(i + di, j + dj)


cnt = 0
for i in range(h):
    for j in range(w):
        if not seen[i][j] and s[i][j] == "#":
            dfs(i, j)
            cnt += 1

print(cnt)
