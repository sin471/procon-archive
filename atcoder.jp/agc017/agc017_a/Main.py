n, p = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(2)]

# dp[i][j]:=(a1...ajの中からいくつか選んだ総和)%2=iとなる組み合わせの数
dp[0][0] = 1
for i in range(n):
    if a[i] % 2 == 0:
        dp[0][i + 1] += dp[0][i] * 2
        dp[1][i + 1] += dp[1][i] * 2
    else:
        dp[1][i + 1] += dp[0][i] + dp[1][i]
        dp[0][i + 1] += dp[1][i] + dp[0][i]

print(dp[p][-1])
