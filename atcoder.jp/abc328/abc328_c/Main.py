n, q = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]

acc = [0] * (n + 1)
for i in range(1, n):
    acc[i + 1] = acc[i]
    if s[i - 1] == s[i]:
        acc[i + 1] += 1

for li, ri in lr:
    print(acc[ri] - acc[li])
