n, m = map(int, input().split())

a = []
for i in range(m):
    c_i = int(input())
    a.append(list(map(int, input().split())))

sample = set(range(1, n + 1))

ans = 0
for i in range(1,1 << m):
    s = set()
    for j in range(m):
        bit = i & (1 << j)
        if bit:
            s.update(set(a[j]))
    if s == sample:
        ans += 1

print(ans)
