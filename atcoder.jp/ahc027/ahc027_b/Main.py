import sys

sys.setrecursionlimit(1000000)
N = int(input())
h = [input() for _ in range(N - 1)]
v = [input() for _ in range(N)]
d = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
DIJ = [(0, -1), (0, 1), (-1, 0), (1, 0)]
DIR = "LRUD"


def dfs(i, j):
    visited[i][j] = True

    scores = [[float("-INf"), -1]] * 4
    for dir in range(4):
        di, dj = DIJ[dir]
        i2 = i + di
        j2 = j + dj

        if (0 <= i2 < N and 0 <= j2 < N and not visited[i2][j2]) and (
            (di == 0 and v[i][min(j, j2)] == "0")
            or (dj == 0 and h[min(i, i2)][j] == "0")
        ):
            scores[dir] = [d[i2][j2], dir]

    for _ in range(4):
        dir = max(scores)[1]
        di, dj = DIJ[dir]
        i2 = i + di
        j2 = j + dj
        if dir == -1:
            return
        print(DIR[dir], end="")
        dfs(i2, j2)
        scores[dir] = [float("-INF"), -1]

        print(DIR[(dir + 1) % 2 + (dir // 2) * 2], end="")


dfs(0, 0)
print()
