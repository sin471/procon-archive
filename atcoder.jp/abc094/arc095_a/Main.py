n = int(input())

x = list(map(int, input().split()))

sorted_x = sorted(x)

mid = n // 2

for i in x:
    if i <= sorted_x[mid - 1]:
        print(sorted_x[mid])
    else:
        print(sorted_x[mid - 1])
