n, d = map(int, input().split())
s = [list(input()) for _ in range(n)]

ts=list(zip(*s))
cnt = 0
ans = 0
for i in [all(map(lambda char: char == "o", ts_i)) for ts_i in ts]:
    if i:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)

print(ans)
