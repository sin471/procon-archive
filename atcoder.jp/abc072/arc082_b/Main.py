from math import ceil

n = int(input())
p = list(map(lambda x: int(x) - 1, input().split()))
cnt = 0
ans = 0
for i in range(n):
    if p[i] == i:
        cnt += 1
    else:
        ans += ceil(cnt / 2)
        cnt = 0

ans += ceil(cnt / 2)

print(ans)
