n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 2 for _ in range(n + 1)]

for i in range(n):
    x, y = xy[i]
    if x == 0:
        dp[i + 1][0] = max(dp[i][0] + max(y, 0), dp[i][1] + y)
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = max(dp[i][0] + y, dp[i][1])

print(max(dp[-1]))
