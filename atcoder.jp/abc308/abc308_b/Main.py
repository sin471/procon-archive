n, m = map(int, input().split())
c = input().split()
d = input().split()
p = list(map(int, input().split()))

price = dict()
for i in range(m):
    price[d[i]] = p[i + 1]
ans = 0
for c_i in c:
    ans += price.get(c_i, p[0])

print(ans)
