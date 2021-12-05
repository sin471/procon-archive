a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

flags = [[0]*3 for _ in range(3)]

ans = "No"
for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            flags[i][j] = 1

for i in flags:
    if sum(i) == 3:
        ans = "Yes"

for i in zip(*flags):
    if sum(i) == 3:
        ans = "Yes"

sum_ = 0
for i in range(3):
    sum_ += flags[i][i]

if sum_ == 3:
    ans = "Yes"

sum_ = 0
for i in range(3):
    sum_ += flags[i][2-i]

if sum_ == 3:
    ans = "Yes"

print(ans)
