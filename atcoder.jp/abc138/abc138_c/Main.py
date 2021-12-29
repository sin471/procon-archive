import heapq
n = int(input())
v = list(map(int, input().split()))

heapq.heapify(v)

while len(v) > 1:
    a = heapq.heappop(v)
    b = heapq.heappop(v)
    heapq.heappush(v, (a+b)/2)

print(v[0])
