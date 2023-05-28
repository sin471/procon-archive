n = int(input())
b = list(map(int, input().split()))

l = []
for i in range(n):
    x = len(b)
    for j in range(x - 1, -1, -1):
        if b[j] == j + 1:
            del b[j]
            l.append(j + 1)
            break

if len(b) == 0:
    print(*l[::-1])
else:
    print(-1)
