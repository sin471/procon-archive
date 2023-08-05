n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

l = [0] * n

for a, b in ab:
    if l[a - 1] >= 0:
        l[a - 1] = 1
    l[b - 1] = -1

l2 = [i for i, l_i in enumerate(l, 1) if l_i == 1]

print(l2[0]) if len(l2)==1 else print(-1)
