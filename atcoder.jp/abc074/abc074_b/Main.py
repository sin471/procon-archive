n = int(input())
k = int(input())
x = map(int, input().split())

dist = 0

for i in x:
    dist += min(abs(k-i), i)*2

print(dist)
