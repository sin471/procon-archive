n = int(input())

d = {}
original_max = -1
ind = -1
for i in range(1, n + 1):
    tmp = input().split()
    s, t = tmp[0], int(tmp[1])

    if d.get(s, False) is False and original_max < t:
        original_max = max(original_max, t)
        ind = i
    d[s] = t

print(ind)
