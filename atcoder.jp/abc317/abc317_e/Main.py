from collections import deque

h, w = map(int, input().split())
h += 2
w += 2

a = [list("#" + input() + "#") if 0 < i < h - 1 else list("#" * w) for i in range(h)]

q = deque()
sx = sy = 0
gx = gy = 0
dxy = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
for i in range(h):
    for j in range(w):
        a_ij = a[i][j]
        if a_ij == "S":
            sx, sy = i, j
        if a_ij == "G":
            gx, gy = i, j
            a[i][j] = "."


        dx, dy = dxy.get(a_ij, (0, 0))
        if dx == dy == 0:
            continue

        i2, j2 = i + dx, j + dy
        while a[i2][j2] in "!.":
            a[i2][j2] = "!"
            i2 += dx
            j2 += dy

q.append((sx, sy))

dists = [[-1] * w for _ in range(h)]
dists[sx][sy] = 0

while q:
    x, y = q.popleft()
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        x2, y2 = x + dx, y + dy
        if dists[x2][y2] == -1 and a[x2][y2] == ".":
            q.append((x2, y2))
            dists[x2][y2] = dists[x][y] + 1

print(dists[gx][gy])
