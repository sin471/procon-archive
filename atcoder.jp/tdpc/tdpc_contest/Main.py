n = int(input())
p = list(map(int, input().split()))
dp = [[0]*(sum(p)+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
    for j in range(sum(p)):
        if not dp[i][j]:
            continue

        dp[i+1][j] = 1
        dp[i+1][j+p[i]] = 1


print(sum(dp[-1]))
