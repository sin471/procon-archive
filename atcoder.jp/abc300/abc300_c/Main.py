h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
s = [0] * min(h, w)
d = [[0, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

for i in range(1, h - 1):
    for j in range(1, w - 1):
        if all(c[i + dx][j + dy] == "#" for dx, dy in d):
            cnt = 0
            i2, j2 = i, j
            while i2 + 1 < h and j2 + 1 < w and c[i2 + 1][j2 + 1] == "#":
                cnt += 1
                i2 += 1
                j2 += 1

            s[cnt - 1] += 1

print(*s)
