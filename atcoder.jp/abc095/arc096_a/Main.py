a,b,c,x,y=map(int,input().split())

ans=0

min_xy=min(x,y)
max_xy=max(x,y)

if a+b>=c*2:
  ans+=c*2*min_xy
else:
  ans+=a*min_xy
  ans+=b*min_xy

remain=max_xy-min_xy

p= a if max_xy==x else b

if remain*c*2<=remain*p:
  ans+=remain*c*2
else:
  ans+=remain*p

print(ans)
