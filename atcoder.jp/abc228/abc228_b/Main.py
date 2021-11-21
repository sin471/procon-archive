n,x=map(int,input().split())
a=list(map(int,input().split()))

friends=[False]*n

i=x
while not friends[i-1]:
  friends[i-1]=True
  i=a[i-1]
  
print(sum(friends))