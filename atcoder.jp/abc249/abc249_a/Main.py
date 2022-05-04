a,b,c,d,e,f,x=map(int,input().split())

def dist(go,velocity,stay,x):
  dist=0
  while x!=0:
    time=min(go,x)
    dist+=time*velocity
    x-=time
    x-=min(stay,x)
    
  return dist
 
takahashi=dist(a,b,c,x)
aoki=dist(d,e,f,x)

if takahashi==aoki:
  ans="Draw"
elif takahashi>aoki:
  ans="Takahashi"
else:
  ans="Aoki"
print(ans)
  