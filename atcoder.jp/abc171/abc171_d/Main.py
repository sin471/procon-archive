n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for _ in range(q)]

l = [0] * (10**5 + 1)

for ai in a:
    l[ai] += 1

s = sum(a)
for bi, ci in bc:
    s -= bi * l[bi]
    s += ci * l[bi]
    l[ci] += l[bi]
    l[bi] = 0
    print(s)

