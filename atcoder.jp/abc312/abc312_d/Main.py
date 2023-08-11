s = input()
n = len(s)
dp = [[0] * (n + 2) for _ in range(n + 1)]

mod = 998244353

if s[0] in "(?":
    dp[1][1] += 1

for i in range(n):
    for j in range(n + 1):
        if s[i] in "?)" and j - 1 >= 0:
            dp[i + 1][j - 1] += dp[i][j]
            dp[i + 1][j - 1] %= mod
        if s[i] in "?(":
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= mod

print(dp[n][0] % mod)
