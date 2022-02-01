n, l, w = map(int, input().split())
a = list(map(int, input().split()))

a.append(l)
cnt = 0
r = 0

for x in a:
    if x > r:
        cnt += int((x-r+w-1)//w)
    r = x+w

print(cnt)
