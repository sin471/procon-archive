n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]

exist = [0] * n
balls = [1] * n
exist[0] = 1

for x, y in xy:
    if exist[x - 1]:
        exist[y - 1] = 1

    balls[x - 1] -= 1
    balls[y - 1] += 1
    if balls[x - 1] == 0:
        exist[x - 1] = 0

print(sum(exist))
