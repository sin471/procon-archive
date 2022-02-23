from collections import deque

n = int(input())
a = list(map(int, input().split()))
q = deque()

count = 0

for ai in a:
    if len(q) == 0 or q[-1][0] != ai:
        q.append([ai, 1])
        count += 1

    elif q[-1][0] == ai:
        ele = q.pop()
        ele[1] += 1
        count += 1
        q.append(ele)

    if q[-1][1] == q[-1][0]:
        count -= q.pop()[1]

    print(count)
