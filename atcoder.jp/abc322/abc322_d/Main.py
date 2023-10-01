from copy import deepcopy

ps = []
for _ in range(3):
    ps.append([list(input()) for _ in range(4)])


def rotate(p):
    p2 = [["."] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            p2[3 - j][i] = p[i][j]
    return p2


grid = [["."] * 4 for _ in range(4)]


def is_inside(x, y):
    return 0 <= x < 4 and 0 <= y < 4


def put(grid, p, x, y):
    for i in range(4):
        for j in range(4):
            if p[i][j] == ".":
                continue
            if not is_inside(x + i, y + j) or grid[x + i][y + j] == "#":
                return False

            grid[x + i][y + j] = "#"

    return True


filled = [["#"] * 4 for _ in range(4)]


def dfs(n, ps, grid):
    if n == 3:
        return grid == filled

    res = False
    for x in range(-3, 4):
        for y in range(-3, 4):
            grid2 = deepcopy(grid)
            if put(grid2, ps[n], x, y):
                res |= dfs(n + 1, ps, grid2)
    return res


def solve():
    for _ in range(4):
        ps[1] = rotate(ps[1])
        for _ in range(4):
            ps[2] = rotate(ps[2])
            grid = [["."] * 4 for _ in range(4)]
            if dfs(0, ps, grid):
                return True
    return False


print("Yes" if solve() else "No")
