import heapq

n, k = map(int, input().split())
a = list(map(int, input().split()))

q = [0]
heapq.heapify(q)
ans = [-1] * (k + 2)

i = 1
while True:
    if ans[k + 1] != -1:
        print(ans[k + 1])
        break

    v = heapq.heappop(q)
    if ans[i - 1] == v:
        continue
    ans[i] = v
    i += 1
    for a_i in a:
        heapq.heappush(q, a_i + v)
