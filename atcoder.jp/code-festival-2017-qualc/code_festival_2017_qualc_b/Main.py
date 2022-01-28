n = int(input())
a = list(map(int, input().split()))

odd = 2 if a[0] % 2 == 0 else 1


for i in range(1, n):
    if a[i] % 2 == 0:
        odd *= 2

print(3**n-odd)
