n, m, p = map(int, input().split())

d = m
cnt = 0
while d <= n:
    d += p
    cnt += 1

print(cnt)
