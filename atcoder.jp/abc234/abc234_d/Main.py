import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))

q=p[:k]
heapq.heapify(q)
tmp = heapq.heappop(q)
print(tmp)
heapq.heappush(q, tmp)

for i in range(k, n):
    a = heapq.heappop(q)
    a = max(p[i], a)
    heapq.heappush(q,a)
    
    ans=heapq.heappop(q)
    print(ans)
    heapq.heappush(q,ans)
