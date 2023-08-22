import pypyjit
import sys
pypyjit.set_param('max_unroll_recursion=0')

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

has_reached = [[0] * m for _ in range(n)]
has_stopped = [[0] * m for _ in range(n)]


def dfs(i, j, di, dj):
    global has_reached
    global has_stopped

    has_reached[i][j] = 1
    if s[i + di][j + dj] == "#":
        if not has_stopped[i][j]:
            has_stopped[i][j] = 1
            for di2, dj2 in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if s[i + di2][j + dj2] != "#":
                    dfs(i + di2, j + dj2, di2, dj2)
    else:
        dfs(i + di, j + dj, di, dj)

dfs(1, 1, -1, 0)
print(sum(sum(l_i) for l_i in has_reached))
