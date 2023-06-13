n, q = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]

acc = [0] * n
for i in range(1, n):
    acc[i] = acc[i - 1]
    if s[i - 1] + s[i] == "AC":
        acc[i] += 1

for l, r in lr:
    print(acc[r - 1] - acc[l - 1])
