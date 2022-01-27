n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = 0
for i in range(n):
    if a[i] >= b[i]:
        total += b[i]
        a[i] -= b[i]

    elif a[i]+a[i+1] > b[i]:
        total += b[i]
        a[i+1] -= (b[i]-a[i])


    elif a[i]+a[i+1] <= b[i]:
        total += a[i]+a[i+1]
        a[i]=0
        a[i+1] = 0


print(total)
