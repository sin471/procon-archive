l, r = map(int, input().split())

ans = float("INF")
for i in range(l, r):
    for j in range(i + 1, r + 1):
        ans = min((i * j) % 2019, ans)
        if ans == 0:
            print(0)
            exit()
print(ans)

