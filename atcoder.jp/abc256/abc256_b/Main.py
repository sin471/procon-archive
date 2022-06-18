n=int(input())
a=list(map(int,input().split()))
grid=[0]*4
p=0
for a_i in a:
  grid[0]=1
  for  j in range(3,-1,-1):
    if not grid[j]:
      continue
    if j+a_i>=4:
      p+=1
      grid[j]=0
    else:
      grid[j+a_i]=1
      grid[j]=0

print(p)
      
    
  