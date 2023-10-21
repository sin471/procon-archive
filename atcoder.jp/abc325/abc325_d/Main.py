import heapq
from bisect import bisect_left

n = int(input())
td = [list(map(int, input().split())) for _ in range(n)]
td.sort()

t = []
d = []
for x, y in td:
    t.append(x)
    d.append(y)

cnt = 0

q = []
heapq.heapify(q)
i = 0
tim = t[0]

while True:
    while i < n and t[i] <= tim:
        heapq.heappush(q, t[i] + d[i])
        i += 1

    if q:
        x = heapq.heappop(q)
        if tim <= x:
            cnt += 1
            tim += 1
    else:
        if i == n:
            break
        tim = t[bisect_left(t, tim)]


print(cnt)
