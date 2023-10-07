n = int(input())
s = [list(input()) for _ in range(n)]

cnt = [[0, -i] for i in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == "o":
            cnt[i][0] += 1

for _, i in sorted(cnt, reverse=True):
    print(-i + 1, end=" ")
