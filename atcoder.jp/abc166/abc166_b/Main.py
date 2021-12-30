n, k = map(int, input().split())
a = []
for i in range(k):
    _ = int(input())
    a.append(list(map(int, input().split())))

flags = [0]*n

for i in a:
    for j in i:
        if not flags[j-1]:
            flags[j-1] = 1

print(n-sum(flags))
