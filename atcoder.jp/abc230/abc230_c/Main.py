n,a,b=map(int,input().split())
p,q,r,s=map(int,input().split())

l=[]

#y=x+intercept1
#y=-x+intercept2
#(y,x)は上からy行目,左からx列目を表す
intercept1=a-b
intercept2=a+b
for y in range(p,q+1):
    l2=[]
    for x in range(r,s+1):
        if y==x+intercept1 or y==-x+intercept2:
            l2.append("#")
        else:
            l2.append(".")
    l.append(l2)


for i in l:
    print(*i,sep="")
