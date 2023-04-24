from collections import deque

n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t = deque(sorted(t))
ans = 0
while t:
    t_head = t.popleft()
    ans += 1
    c2 = c - 1
    while len(t) != 0 and t[0] <= t_head + k and c2 != 0:
        t.popleft()
        c2 -= 1
print(ans)
