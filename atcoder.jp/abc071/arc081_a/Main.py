n = int(input())
a = list(map(int, input().split()))
d = dict()

l = []

for a_i in a:
    d.setdefault(a_i, 0)
    d[a_i] += 1
    if d[a_i] == 2:
        d[a_i] = 0
        l.append(a_i)

l.sort(reverse=True)
if len(l) >= 2:
    print(l[0] * l[1])
else:
    print(0)
