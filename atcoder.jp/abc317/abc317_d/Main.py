from math import ceil

n = int(input())
lis = []
sumz = 0
for i in range(n):
    x, y, z = map(int, input().split())
    traitor = max(ceil((y - x) / 2), 0)
    lis.append((x, y, z, traitor))
    sumz += z

INF = float("INF")
dp = [[INF] * (sumz + 1) for _ in range(n + 1)]

# dp[i][j]=i番目までの選挙区で議席をjにするのに必要な最小の鞍替え人数

dp[0][0] = 0
for i, (x, y, z, new_traitor) in enumerate(lis, 1):
    for j in range(sumz + 1):
        traitor = dp[i - 1][j]
        if traitor == INF:
            continue
        if j + z >= sumz + 1:
            continue
        dp[i][j] = min(traitor, dp[i][j])
        dp[i][j + z] = min(traitor + new_traitor, dp[i][j + z])  # type: ignore


print(min(dp[-1][ceil(sumz / 2) :]))
