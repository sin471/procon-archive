n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

l = [[] for _ in range(10**5+1)]

for a, b in ab:
    l[a].append(b)
    l[b].append(a)


ans = 0
for i, l_i in enumerate(l):
    cnt = 0
    for l_ij in l_i:
        if l_ij < i:
            cnt += 1
    if cnt == 1:
        ans += 1

print(ans)
