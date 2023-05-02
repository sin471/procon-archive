from collections import defaultdict
from itertools import combinations

n = int(input())
s = [input() for _ in range(n)]

d = defaultdict(int)

for s_i in s:
    head = s_i[0]
    if head in "MARCH":
        d[head] += 1

ans = 0
for keys in combinations("MARCH", 3):
    ans += d[keys[0]] * d[keys[1]] * d[keys[2]]

print(ans)
