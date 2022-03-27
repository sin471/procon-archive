n = int(input())
a = list(set(map(int, input().split())))

a.sort()

for i in range(len(a)):
    if i != a[i]:
        print(i)
        break
else:
    print(len(a))
