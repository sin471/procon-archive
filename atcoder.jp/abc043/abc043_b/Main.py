from collections import deque

s = input()
q = deque()

for i in s:
    if i == "B" and len(q):
        q.pop()

    elif i == "0":
        q.append("0")

    elif i == "1":
        q.append("1")

print("".join(q))
