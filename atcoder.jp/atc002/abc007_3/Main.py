from collections import deque

r, c = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
grid = [list(input()) for _ in range(r)]

ans_grid = [[-1] * c for _ in range(r)]
ans_grid[sx - 1][sy - 1] = 0
grid[sx - 1][sy - 1] = "@"
q = deque()
q.append((sx - 1, sy - 1))


while q:
    x, y = q.popleft()
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if grid[x + dx][y + dy] == ".":
            q.append((x + dx, y + dy))
            grid[x + dx][y + dy] = "@"
            ans_grid[x + dx][y + dy] = ans_grid[x][y] + 1

# from pprint import pprint

# pprint(grid)
# pprint(ans_grid)
print(ans_grid[gx - 1][gy - 1])
