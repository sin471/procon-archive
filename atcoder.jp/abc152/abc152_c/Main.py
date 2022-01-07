n = int(input())
p = list(map(int, input().split()))

min_l = [0]*n
min_l[0] = p[0]

for i in range(1, n):
    min_l[i] = min(p[i], min_l[i-1])

cnt = 0

for i in range(n):
    if min_l[i] == p[i]:
        cnt += 1

print(cnt)
