n = int(input())
a = list(map(int, input().split()))

cnt = [0] * n
ans = []
for i in a:
    cnt[i - 1] += 1
    if cnt[i - 1] == 2:
        ans.append(i)

print(*ans)
