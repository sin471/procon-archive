_ = int(input())
a = [0] + list(map(int, input().split())) + [0]
n = len(a)

cost = 0
for i in range(1, n):
    cost += abs(a[i] - a[i - 1])

for i in range(1, n - 1):
    cost2 = cost
    cost2 += abs(a[i - 1] - a[i + 1])
    cost2 -= abs(a[i] - a[i - 1]) + abs(a[i + 1] - a[i])
    print(cost2)
