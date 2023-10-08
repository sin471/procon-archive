import heapq

n = int(input())
s = []
d = dict()
for i in range(n):
    x, y = list(map(int, input().split()))
    s.append(x)
    d[x] = y

heapq.heapify(s)

ans = 0


while s:
    si = heapq.heappop(s)
    ci = d.get(si, 0)

    ans += ci % 2
    if ci >= 2:
        si2 = si * 2
        ci2 = ci // 2
        if d.get(si2):
            d[si2] += ci2
            continue

        heapq.heappush(s, si2)
        d[si2] = ci2

print(ans)
