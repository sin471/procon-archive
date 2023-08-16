n = int(input())
s = list(input())
q = int(input())
txc = []

for _ in range(q):
    t, x, c = input().split()
    txc.append((int(t), int(x), c))

is_upper = None

last = -1
for i in range(q - 1, -1, -1):
    if txc[i][0] != 1:
        last = i
        break

for i, (t, x, c) in enumerate(txc):
    if t == 1:
        s[x - 1] = c
    elif t == 2:
        is_upper = False
    elif t == 3:
        is_upper = True
    if i == last:
        if is_upper is False:
            s = [s_i.lower() for s_i in s]
        elif is_upper is True:
            s = [s_i.upper() for s_i in s]

print("".join(s))
