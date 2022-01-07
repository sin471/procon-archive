s = list(input())

ans = float("INF")

for i in [["0", "1"], ["1", "0"]]:
    cnt = 0
    for j in range(len(s)):
        s_i = s[j]
        if j % 2 == 0:
            if s_i == i[0]:
                cnt += 1
        elif j % 2 == 1:
            if s_i == i[1]:
                cnt += 1
    ans = min(cnt, ans)


print(ans)