n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

sa = sum(a)
for i in range(0, 101):
    s = sa + i - min(a[0], i) - max(a[-1], i)
    if s >= x:
        print(i)
        exit()

print(-1)
