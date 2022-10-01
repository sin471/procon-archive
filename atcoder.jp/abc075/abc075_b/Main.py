h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue

        cnt = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if not (0 <= i + di < h and 0 <= j + dj < w):
                    continue

                if s[i + di][j + dj] == "#":
                    cnt += 1

        s[i][j] = str(cnt)
        

for i in range(h):
    print("".join(s[i]))
