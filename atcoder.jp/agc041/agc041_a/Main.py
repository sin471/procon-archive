n,a,b=map(int,input().split())

if (a+b)%2==0:
  ans=abs(a-(a+b)//2)
  print(ans)
  exit()


to_top=min(a,b)-1
to_worst=n-max(a,b)
to_close_edge=min(to_top,to_worst)+1

a2=a+to_close_edge
b2=b+to_close_edge

ans=abs(a2-(a2+b2)//2)+to_close_edge

print(ans)