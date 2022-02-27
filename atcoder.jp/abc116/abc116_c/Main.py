n = int(input())
h = list(map(int, input().split()))

cnt = 0
h.append(0)

while any(h):
    l = r = 0
    for i in range(n):
        if h[i] != 0:
            l = i
            break
    r=l
    while h[r]!=0:
        h[r]-=1
        r+=1

    cnt += 1

print(cnt)
