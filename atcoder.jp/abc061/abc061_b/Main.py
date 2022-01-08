n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
roads = [0]*n

# 都市nの道路の本数:=roads[n-1]
for a, b in ab:
    roads[a-1] += 1
    roads[b-1] += 1

print(*roads,sep="\n")