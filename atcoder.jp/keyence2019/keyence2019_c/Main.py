n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_a = sum(a)
sum_b = sum(b)
remaining_points = sum_a - sum_b

if sum_a < sum_b:
    print(-1)
    exit()

diffs = sorted([a[i] - b[i] for i in range(n) if a[i] - b[i] >= 0])

same = 0
for diff in diffs:
    if remaining_points - diff >= 0:
        same += 1
        remaining_points -= diff

print(n - same)
