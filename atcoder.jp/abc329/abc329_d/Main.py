n, m = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * n
max_cnt = 0
top = 0
for i in range(m):
    j = a[i] - 1
    c[j] += 1
    if c[j] > max_cnt:
        top = j
        max_cnt = c[j]
    elif c[j] == max_cnt:
        top = j if j < top else top
    print(top + 1)
