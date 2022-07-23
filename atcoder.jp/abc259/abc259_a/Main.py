n,m,x,t,d=map(int,input().split())

if x<=m:
    print(t)
else:
    first=t-d*x
    print(first+m*d)
