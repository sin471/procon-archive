from collections import deque

q = int(input())
tx = [list(map(int, input().split())) for _ in range(q)]

dq = deque()

for t, x in tx:
    if t == 1:
        dq.appendleft(x)
    elif t == 2:
        dq.append(x)
    elif t==3:
        print(dq[x-1])
