n = int(input())
wx = [list(map(int, input().split())) for _ in range(n)]

ans = 0
wl = [[0] * 24 for _ in range(n)]

for t in range(9, 18):
    cnt = 0
    for i in range(n):
        w, x = wx[i]
        wl[i][(t + x) % 24] = 1


for t in range(24):
    cnt = 0
    for i in range(n):
        if wl[i][t]:
            cnt += wx[i][0]
    ans = max(ans, cnt)

print(ans)
