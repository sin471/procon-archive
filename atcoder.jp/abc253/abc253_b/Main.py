h,w=map(int,input().split())
s=[input() for _ in range(h)]

p=[]
for i in range(h):
    for j in range(w):
        if s[i][j]=="o":
            p.append((i,j))

p1,p2=p[0],p[1]

print(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))
