from collections import defaultdict

n = int(input())
a = [int(input()) for _ in range(n)]

d = defaultdict(int)

for a_i in a:
    d[a_i] += 1

cnt = 0
for values in d.values():
    if values % 2 == 1:
        cnt += 1

print(cnt)
