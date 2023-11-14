n = int(input())
s = input()
atc = "atcoder"
dp = [[0] * (len(atc) + 1) for _ in range(n + 1)]
mod = 10**9 + 7

# dp[i][j]:=1-indexedでSのi文字目までを使って"atcoder"のj文字目までをつくる場合の数
dp[0][0] = 1
for i in range(1, n + 1):
    k = atc.find(s[i - 1]) + 1

    for j in range(len(atc) + 1):
        dp[i][j] += dp[i - 1][j]
        dp[i][j] %= mod

    if k == 0:
        continue
    dp[i][k] += dp[i - 1][k - 1]
    dp[i][k] %= mod
    
print(dp[n][len(atc)] % mod)
