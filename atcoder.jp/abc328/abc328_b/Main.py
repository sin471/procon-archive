n = int(input())
d = list(map(int, input().split()))

ans = 0
for i, di in enumerate(d, 1):
    for dij in range(1, di + 1):
        if len(set(str(dij) + str(i))) == 1:
            ans += 1

print(ans)
