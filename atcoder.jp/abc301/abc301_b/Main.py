n = int(input())
a = list(map(int, input().split()))

l = []

for i in range(1, n):
    elem = a[i - 1]
    l.append(elem)
    while abs(elem - a[i]) > 1:
        if elem < a[i]:
            elem += 1
        elif elem > a[i]:
            elem -= 1
        l.append(elem)

l.append(a[-1])
print(*l)
