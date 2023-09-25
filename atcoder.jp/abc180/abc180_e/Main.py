n = int(input())
xyz = [list(map(int, input().split())) for _ in range(n)]

INF = float("INF")
dp = [[INF] * n for _ in range(1 << n)]

graph = [[0] * n for _ in range(n)]


def dist(a, b, c, p, q, r):
    return abs(p - a) + abs(q - b) + max(0, r - c)


for i, (x1, y1, z1) in enumerate(xyz):
    for j, (x2, y2, z2) in enumerate(xyz):
        graph[i][j] = dist(x1, y1, z1, x2, y2, z2)

dp[1][0] = 0
for bits in range(1, 1 << n):
    for i in range(n):
        for j in range(n):
            next_bits = bits | (1 << i)
            dp[next_bits][i] = min(dp[bits][j] + graph[j][i], dp[next_bits][i])

print(dp[-1][0])