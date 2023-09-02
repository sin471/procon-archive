h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

cnt = 0
for i in range(h - 1):
    for j in range(w - 1):
        diff = b[i][j] - a[i][j]
        cnt += abs(diff)
        for dx, dy in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            a[i + dx][j + dy] += diff

if a == b:
    print("Yes")
    print(cnt)
else:
    print("No")
