from collections import deque

h, w = map(int, input().split())
rs, cs = map(lambda x: int(x) - 1, input().split())
rt, ct = map(lambda x: int(x) - 1, input().split())

s = [list(input()) for _ in range(h)]

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def is_inside(x, y, h, w):
    return 0 <= x < h and 0 <= y < w


INF = 10**6
grid = [[[INF] * 4 for _ in range(w)] for _ in range(h)]


q = deque()

for k in range(4):
    grid[rs][cs][k] = 0
    q.append([rs, cs, k])

while q:
    x, y, i = q.popleft()
    dx, dy = d[i]
    x2, y2 = x + dx, y + dy
    if not (is_inside(x2, y2, h, w) and s[x2][y2] == "."):
        continue

    for j in range(4):
        cost = grid[x][y][i] + (0 if i == j else 1)
        if grid[x2][y2][j] <= cost:
            continue
        if i == j:
            q.appendleft([x2, y2, j])
        else:
            q.append([x2, y2, j])
        grid[x2][y2][j] = cost

print(min(grid[rt][ct]))
