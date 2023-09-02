from collections import deque

n = int(input())
a = list(map(int, input().split()))

s = sum(a)
if s % 10 != 0:
    print("No")
    exit()

q = deque()
temp = 0
i = 0
x = s // 10
n2 = n * 2
while i < n2:
    while temp < x:
        q.append(a[i % n])
        temp += a[i % n]
        i += 1
    while temp > x:
        temp -= q.popleft()
    if temp == x:
        print("Yes")
        exit()

print("No")
