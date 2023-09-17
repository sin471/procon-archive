import heapq

n, m = map(int, input().split())
tws = [list(map(int, input().split())) for _ in range(m)]

q = tws
p = list(range(n))
heapq.heapify(q)
heapq.heapify(p)

ws = [0] * n
while q:
    event = heapq.heappop(q)
    if len(event) == 3 and p:
        t, w, s = event
        person = heapq.heappop(p)
        heapq.heappush(q, [t + s, -person])
        ws[person] += w
    elif len(event) == 2:
        t, person = event[0], -event[1]
        heapq.heappush(p, person)

print(*ws, sep="\n")
