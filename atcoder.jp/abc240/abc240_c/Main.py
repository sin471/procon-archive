n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*10001 for i in range(n+1)]

dp[0][0] = 1

for i in range(1, n+1):
    for j in range(10001):
        if not dp[i-1][j]:
            continue
        a, b = ab[i-1]

        if j+a <= 10000:
            dp[i][j+a] = 1

        if j+b <= 10000:
            dp[i][j+b] = 1

print("Yes" if dp[n][x] else "No")
