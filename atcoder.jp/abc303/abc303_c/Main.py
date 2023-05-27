n, m, h, k = map(int, input().split())
s = input()
tmp = [list(map(int, input().split())) for _ in range(m)]
d = dict()

for x, y in tmp:
    d.setdefault(x, set())
    d[x].add(y)

takahashi = [0, 0]

for s_i in s:
    if s_i == "U":
        takahashi[1] += 1
    elif s_i == "D":
        takahashi[1] -= 1
    elif s_i == "L":
        takahashi[0] -= 1
    elif s_i == "R":
        takahashi[0] += 1
    h -= 1

    if h < 0:
        print("No")
        exit()

    x, y = takahashi
    if (y in d.get(x, {None})) and h < k:
        h = k
        d[x].remove(y)


print("Yes")
