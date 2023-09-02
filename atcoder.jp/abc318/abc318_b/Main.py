n = int(input())
abcd = [list(map(int, input().split())) for _ in range(n)]

l = [[0] * (100) for _ in range(100)]


for a, b, c, d in abcd:
    for i in range(a, b):
        for j in range(c, d):
            l[i][j] = 1

print(sum(sum(l_i) for l_i in l))
