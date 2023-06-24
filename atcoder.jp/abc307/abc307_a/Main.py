n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    s = 0
    for j in range(7):
        s += a[i * 7 + j]
    print(s)
