a, b, k = map(int, input().split())

s = set()
for i in range(a, a+k):
    if i <= b:
        s.add(i)

for i in range(b, b-k, -1):
    if i >= a:
        s.add(i)

l = sorted(list(s))
print(*l, sep="\n")
