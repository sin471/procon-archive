m = int(input())
s1 = list(input())
s2 = list(input())
s3 = list(input())

if not set(s1).intersection(set(s2), set(s3)):
    print(-1)
    exit()


l1 = [[] for _ in range(10)]
l2 = [[] for _ in range(10)]
l3 = [[] for _ in range(10)]

for t in range(m):
    for s, l in [(s1, l1), (s2, l2), (s3, l3)]:
        x = int(s[t])
        l[x].append(t)
        l[x].append(t + m)
        l[x].append(t + 2 * m)

ans = float("INF")
for d in range(10):
    for l1i in l1[d]:
        for l2j in l2[d]:
            for l3k in l3[d]:
                if not (l1i != l2j and l2j != l3k and l1i != l3k):
                    continue
                ans = min(ans, max(l1i, l2j, l3k))

print(ans)
