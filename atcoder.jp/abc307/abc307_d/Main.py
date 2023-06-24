from collections import deque

n = int(input())
s = list(input())
q = deque()

lrs = []
for i in range(n):
    if s[i] == "(":
        q.append(i)
    if s[i] == ")" and len(q):
        l = q.pop()
        r = i
        lrs.append((l, r))

lrs.sort()
j = 0

for i in range(len(lrs)):
    l, r = lrs[i]
    if j < l:
        j = l
    while j <= r and j < len(s):
        s[j] = "#"
        j += 1

print("".join([x for x in s if x != "#"]))
