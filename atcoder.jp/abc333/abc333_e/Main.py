n = int(input())
tx = [list(map(int, input().split())) for _ in range(n)]

monsters = [0] * n
ans = 0
cnt = 0
l = []

for i in range(n - 1, -1, -1):
    t, x = tx[i]
    if t == 1:
        if monsters[x - 1] > 0:
            monsters[x - 1] -= 1
            cnt -= 1
            l.append(1)
        else:
            l.append(0)
    else:
        monsters[x - 1] += 1
        cnt += 1
    ans = max(ans, cnt)

if not all(monsters[i] == 0 for i in range(n)):
    print(-1)
    exit()

print(ans)
print(*l[::-1])
