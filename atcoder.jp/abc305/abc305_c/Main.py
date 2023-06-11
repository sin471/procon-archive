h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]


d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for i in range(h):
    for j in range(w):
        cnt = 0
        if s[i][j] == ".":
            for dx, dy in d:
                i2 = i + dx
                j2 = j + dy
                if 0 <= i2 < h and 0 <= j2 < w and s[i2][j2] == "#":
                    cnt += 1
            if cnt >= 2:
                print(i + 1, j + 1)
                exit()
