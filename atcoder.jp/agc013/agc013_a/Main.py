n = int(input())
a = list(map(int, input().split()))

cnt = 0
i = 0

while i < n:
    while i + 1 < n and a[i] == a[i + 1]:
        i += 1

    if i + 1 < n and a[i] < a[i + 1]:
        while i + 1 < n and a[i] <= a[i + 1]:
            i += 1

    elif i + 1 < n and a[i] > a[i + 1]:
        while i + 1 < n and a[i] >= a[i + 1]:
            i += 1

    cnt += 1
    i += 1

print(cnt)
