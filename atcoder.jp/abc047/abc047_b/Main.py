w, h, n = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(n)]

area = [[1] * w for _ in range(h)]

for x, y, a in xya:
    for i in range(h):
        for j in range(w):
            if a == 1 and j < x:
                area[i][j] = 0
            elif a == 2 and j >= x:
                area[i][j] = 0
            elif a == 3 and i < y:
                area[i][j] = 0
            elif a == 4 and i >= y:
                area[i][j] = 0

print(sum(map(sum, area)))
