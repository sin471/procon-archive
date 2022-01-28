from operator import itemgetter

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(key=itemgetter(0))

ans = 0
for a, b in ab:
    if b-m >= 0:
        ans += (m*a)
        break

    elif m-b > 0:
        ans += (b*a)
        m -= b

print(ans)
