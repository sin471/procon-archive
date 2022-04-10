n = int(input())
s = [int(input()) for _ in range(n)]

sum_s = sum(s)
dp = [[0]*(sum_s+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
    for j in range(sum_s+1):
        if not dp[i][j]:
            continue

        dp[i+1][j] = 1
        dp[i+1][j+s[i]] = 1

ans = 0
for i in range(sum_s+1):
    if (not dp[-1][i]) or i % 10 == 0:
        continue

    ans = max(ans, i)

print(ans)
