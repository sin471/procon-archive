from collections import deque

s = deque(input())
s2 = []
tmp = []

abc = ["A", "B", "C"]
next_ = 0
i = 0
for _ in range(len(s)):
    s2.append(s.popleft())
    if s2[-3:] == abc:
        for _ in range(3):
            s2.pop()


print("".join(s2))
