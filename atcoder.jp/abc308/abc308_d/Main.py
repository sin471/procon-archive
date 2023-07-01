import sys

sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

chars = "snuke"

seen = [[0] * w for _ in range(h)]


def is_inside(x, y, h=h, w=w):
    return 0 <= x < h and 0 <= y < w


def dfs(x, y, c):
    global seen
    if is_inside(x, y) and s[x][y] == chars[c]:
        seen[x][y] = 1
    else:
        return

    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        next_c = (c + 1) % 5

        if not is_inside(x + dx, y + dy) or seen[x + dx][y + dy]:
            continue
        dfs(x + dx, y + dy, next_c)


dfs(0, 0, 0)
print("Yes" if seen[h - 1][w - 1] else "No")
