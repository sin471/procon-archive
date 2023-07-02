n = int(input())
a = list(map(int, input().split()))
s = list(input())


sa = [s[i] + str(a[i]) for i in range(n)]

l = []

for i in "012":
    for j in "012":
        for k in "012":
            l.append(["M" + i, "E" + j, "X" + k])

t = set(range(0, 3))
ans = 0
for l_i in l:
    dp = [[0] * 3 for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] += dp[i - 1][0]
        dp[i][1] += dp[i - 1][1]
        dp[i][2] += dp[i - 1][2]

        if sa[i - 1] == l_i[0]:
            dp[i][0] += 1
        elif sa[i - 1] == l_i[1]:
            dp[i][1] += dp[i - 1][0]
        elif sa[i - 1] == l_i[2]:
            dp[i][2] += dp[i - 1][1]

    tmp_set = t.difference(int(l_ij[1]) for l_ij in l_i)
    ans += min(tmp_set, default=3) * dp[-1][-1]

print(ans)
