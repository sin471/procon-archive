from collections import deque

s = input()

i = 0
q = deque()
while i < len(s):
    head = s[i]
    j = i
    while j < len(s) and s[j] == head:
        j += 1
    q.append(j - i)
    i = j

ans = [0] * len(s)
for i in range(len(s) - 1):
    if s[i] == "R" and s[i + 1] == "L":
        r = q.popleft()
        l = q.popleft()
        ans[i] += ((r + 1) // 2) + l // 2
        ans[i + 1] += r // 2 + ((l + 1) // 2)


print(*ans)
