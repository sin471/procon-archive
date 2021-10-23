h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]

for i1 in range(h):
    for i2 in range(i1,h):
        for j1 in range(w):
            for j2 in range(j1,w):
                x=a[i1][j1]+a[i2][j2]
                y=a[i2][j1]+a[i1][j2]
                if x>y:
                    print("No")
                    exit()

print("Yes")