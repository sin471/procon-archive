h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]


def solve():
    for i in range(h):
        for j in range(w):
            if grid[i][j] == ".":
                continue

            for x in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                d1, d2 = x
                
                if not ((0 <= i + d1 < h) and (0 <= j + d2 < w)):
                    continue

                if grid[i + d1][j + d2] == "#":
                    break
            else:
                return False
    return True


print("Yes" if solve() else "No")
