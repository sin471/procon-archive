from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)

for i in range(1,n+1):
    d[i] = a[i-1]

cnt = 0
for key,val in d.items():
    if d.get(val) == key:
        d[key]=-1
        d[val]=-1
        cnt += 1

print(cnt)