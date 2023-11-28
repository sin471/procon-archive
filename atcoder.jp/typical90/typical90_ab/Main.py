n = int(input())
xy = []
m = 1000
lr = [list(map(int, input().split())) for _ in range(n)]

s = [[0] * (m + 1) for _ in range(m + 1)]

for lx, ly, rx, ry in lr:
    s[ly][lx] += 1
    s[ry][rx] += 1
    s[ly][rx] -= 1
    s[ry][lx] -= 1


for i in range(m):
    for j in range(m - 1):
        s[i][j + 1] += s[i][j]

for i in range(m):
    for j in range(m - 1):
        s[j + 1][i] += s[j][i]

areas = [0] * n
for i in range(m):
    for j in range(m):
        if s[i][j] == 0:
            continue
        areas[s[i][j] - 1] += 1

print(*areas, sep="\n")
