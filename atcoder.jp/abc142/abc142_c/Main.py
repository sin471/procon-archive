n = int(input())
a = list(map(int, input().split()))

a = list(map(lambda x, y: (x, y), a, range(1, n+1)))

a.sort(key=lambda x: x[0])

for i in a:
    print(i[1], end=" ")
