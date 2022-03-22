n = int(input())
l = list(range(1, 2*(n+1)))

for _ in range(n+1):
    print(l.pop(), flush=True)
    m = int(input())
    if m == 0:
        break
    l.remove(m)
