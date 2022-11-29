n, q = map(int, input().split())
a = list(map(int, input().split()))
txy = [list(map(int, input().split())) for _ in range(q)]

l = [0] * (4 * 10**5 + 100)


head = 2 * 10**5 + 10

for i in range(n):
    l[head + i] = a[i]

for t, x, y in txy:
    if t == 1:
        l[head + x - 1], l[head + y - 1] = l[head + y - 1], l[head + x - 1]
    elif t == 2:
        l[head - 1] = l[head + n - 1]
        l[head + n - 1] = 0
        head -= 1
    elif t == 3:
        print(l[head + x - 1])
