n = int(input())
a = list(map(int, input().split()))
a2 = sorted(a, reverse=True)

s = sum(a)
d = dict()
head = -1
for i in range(n):
    x = a2.pop()
    s -= x
    d[x] = s
    head = x


for i in a:
    print(d[i], end=" ")
