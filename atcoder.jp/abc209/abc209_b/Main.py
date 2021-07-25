n, x = map(int, input().split())

a1 = list(map(int, input().split()))

l = []
for i, j in enumerate(a1):
    if (i+1) % 2 == 0:
        j -= 1
    else:
        pass
    l.append(j)

if sum(l) <= x:
    ans = "Yes"
else:
    ans = "No"
print(ans)
