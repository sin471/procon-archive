K = int(input())
dp = [0] * (K + 1)
dp[0] = 1
mod = 10**9 + 7

if K % 9 != 0:
    print(0)
    exit()

for i in range(K + 1):
    for j in range(1, 10):
        if i - j >= 0:
            dp[i] += dp[i - j] % mod

print(dp[K] % mod)
