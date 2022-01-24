n = int(input())
spi=[input().split()+[i] for i in range(1,n+1)]

l = sorted(spi, key=lambda x: (x[0], -int(x[1])))

for li in l:
    print(li[2])
