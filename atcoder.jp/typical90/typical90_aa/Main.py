n = int(input())
s = [input() for _ in range(n)]

d = dict()

for i in range(n):
    if d.get(s[i], False):
        continue

    d[s[i]] = True
    print(i+1)
