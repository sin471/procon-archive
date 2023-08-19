m = int(input())
d = list(map(int, input().split()))

x = (1 + sum(d)) // 2

s = 0
for i in range(m):
    s += d[i]
    if s >= x:
        day = d[i] - s + x
        if day == 0:
            day += 1
        print(i + 1, day)
        break
