abcde = [int(input()) for i in range(5)]

l = []

for i in abcde:
    if i % 10 != 0:
        x = i+(10-i % 10)
    else:
        x = i
    l.append(x)

ans = float("INF")

for i in range(5):
    element1 = abcde.pop(0)
    element2 = l.pop(0)
    tmp = sum(l)+element1
    ans = min(ans, tmp)
    abcde.append(element1)
    l.append(element2)

print(ans)
