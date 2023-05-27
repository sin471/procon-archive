x, y, z = map(int, input().split())
s = input()

"""
dp[i][is_caps]:=i回目のキーを押すまでにかかる合計時間。is_caps=1ならcapsON
"""

dp = [[0] * 2 for _ in range(len(s) + 1)]

dp[0][1] = z

for i in range(1, len(s) + 1):
    a = {"a": 0, "A": 1}[s[i - 1]]

    dp[i][a] = min(dp[i - 1][a] + x, dp[i - 1][(a + 1) % 2] + z + x)
    dp[i][(a + 1) % 2] = min(
        dp[i - 1][a] + z + x, dp[i - 1][(a + 1) % 2] + y, dp[i - 1][a] + z + y
    )

print(min(dp[len(s)]))
