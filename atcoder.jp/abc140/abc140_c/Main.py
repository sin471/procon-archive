n = int(input())
b = list(map(int, input().split()))

a = [0]*n

for i in range(n):
    # b[i]=max(a[i],a[i+1])
    if i == 0:
        a[i] = b[i]
    elif i == n-1:
        a[i] = b[i-1]
    else:
        a[i] = min(b[i-1], b[i])

print(sum(a))
