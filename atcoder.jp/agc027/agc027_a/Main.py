n, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

ans = 0
for i, ai in enumerate(a, 1):
    x -= ai
    if i == n:
        if x == 0:
            ans += 1
        continue

    if x >= 0:
        ans += 1
    else:
        break
print(ans)
