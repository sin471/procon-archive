n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

l = [[1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            l[i][j] = 0

for i in range(m):
    for j in range(1, n):
        l[a[i][j - 1] - 1][a[i][j] - 1] = 0
        l[a[i][j] - 1][a[i][j - 1] - 1] = 0


print(sum(sum(x) for x in l) // 2)
