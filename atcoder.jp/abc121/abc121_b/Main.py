n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for ai in a:
    sum_ = sum(map(lambda x, y: x*y, ai, b))+c
    if sum_ > 0:
        cnt += 1
print(cnt)
