from itertools import accumulate
n = int(input())

a = [list(map(int, input().split())) for _ in range(2)]

upper = list(accumulate(a[0]))
lower = list(accumulate(a[1]))

ans = float("-INF")

for i in range(n):
    first_to_i = upper[i]
    i_to_last = lower[-1]-lower[i]+a[1][i]

    total = first_to_i+i_to_last

    ans = max(ans, total)

print(ans)
