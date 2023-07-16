from copy import deepcopy

n = int(input())
a = [list(input()) for _ in range(n)]
ans = deepcopy(a)

for i in range(n):
    for j in range(n):
        if i == 0 and 1 <= j:
            ans[i][j] = a[i][j - 1]
        elif 1 <= i and j == n - 1:
            ans[i][j] = a[i - 1][j]
        elif i == n - 1 and j <= n - 2:
            ans[i][j] = a[i][j + 1]
        elif i <= n - 2 and j == 0:
            ans[i][j] = a[i + 1][j]


for i in ans:
    print("".join(i))
