h, w = map(int, input().split())

s = [list(input()) for _ in range(h)]
dp = [[float("INF")] * w for _ in range(h)]

dp[0][0] = 1 if s[0][0] == "#" else 0


def is_inside(x, y, h, w):
    return 0 <= x < h and 0 <= y < w


for i in range(h):
    for j in range(w):
        for di, dj in [[0, -1], [-1, 0]]:
            i2, j2 = i + di, j + dj
            if not is_inside(i2, j2, h, w):
                continue

            sij2 = s[i2][j2]
            sij = s[i][j]

            if sij2 == "." and sij == "#":
                dp[i][j] = min(dp[i2][j2] + 1, dp[i][j])
                continue

            dp[i][j] = min(dp[i2][j2], dp[i][j])


print(dp[h - 1][w - 1])
