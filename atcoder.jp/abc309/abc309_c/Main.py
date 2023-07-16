n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: x[0])

cnt = sum(i[1] for i in ab)

if cnt <= k:
    print(1)
    exit()

for i in range(n):
    cnt -= ab[i][1]
    if cnt <= k:
        print(ab[i][0] + 1)
        exit()
