from collections import deque

n, m = map(int, input().split())
s = list(input())
c = list(map(int, input().split()))

colors = [deque() for _ in range(m)]

for i in range(n):
    colors[c[i] - 1].append(s[i])

for i in range(m):
    colors[i].rotate()

ans_list = []
for i in range(n):
    ans_list.append(colors[c[i] - 1].popleft())

print("".join(ans_list))
