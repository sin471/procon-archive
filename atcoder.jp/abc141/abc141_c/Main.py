n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

correct_nums = [0]*n
for ai in a:
    correct_nums[ai-1] += 1

for i in correct_nums:
    incorrect = q-i
    if k <= incorrect:
        print("No")
    else:
        print("Yes")
