n = int(input())
dp = [[0] * 10 for _ in range(n)]

for i in range(1, 10):
    dp[0][i] = 1

mod = 998244353
for i in range(1, n):
    for j in range(1, 10):
        dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j]
        dp[i][j] %= mod

        if j <= 8:
            dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= mod

print(sum(dp[-1]) % mod)
