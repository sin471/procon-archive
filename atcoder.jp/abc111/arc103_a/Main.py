from collections import Counter

n = int(input())
v = list(map(int, input().split()))
c1 = Counter(v[::2])
c2 = Counter(v[1::2])

ans = float("INF")

if len(c1) == len(c2) == 1:
    if c1.keys() == c2.keys():
        print(n // 2)
    else:
        print(0)
    exit()

for i in c1.most_common(2):
    for j in c2.most_common(2):
        if i[0] != j[0]:
            ans = min(ans, n // 2 - i[1] + n // 2 - j[1])

print(ans)
