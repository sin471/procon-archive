s,t,x=map(int,input().split())

if s>t:
  t+=24  
for i in range(s,t):
  if i%24==x:
    print("Yes")
    exit()
    
print("No")