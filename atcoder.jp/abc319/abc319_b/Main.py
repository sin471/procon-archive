n = int(input())

l = []
for i in range(1, 10):
    if n % i == 0:
        l.append(i)

ans = []
for i in range(n + 1):
    js = [j for j in l if i % (n // j) == 0]
    if js:
        s = str(min(js))
    else:
        s = "-"
    ans.append(s)

print("".join(ans))
