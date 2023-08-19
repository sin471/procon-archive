from collections import defaultdict

ice = defaultdict(list)

n = int(input())
fs = [list(map(int, input().split())) for _ in range(n)]

fs = sorted(fs, key=lambda x: x[1], reverse=True)

f0, s0 = fs[0]

f1, s1 = fs[1]
x1 = x2 = -1

if f0 != f1:
    x0 = s0 + s1
    for f, s in fs[2:]:
        if f == f0:
            x1 = max(s0, s) + min(s0, s) // 2
            break
else:
    x0 = max(s0, s1) + min(s0, s1) // 2
    for f, s in fs[2:]:
        if f != f0:
            x1 = s0 + s
            break

print(max(x0, x1))
