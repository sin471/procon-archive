from collections import deque

s = input()
k = int(input())

q = deque()
ans = 0
k2 = 0

for si in s:
    q.append(si)
    if si == ".":
        k2 += 1
    while k2 > k:
        a = q.popleft()
        if a == ".":
            k2 -= 1

    ans = max(ans, len(q))

print(ans)
