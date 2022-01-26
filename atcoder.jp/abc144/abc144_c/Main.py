n=int(input())

def find_divisor_pairs(n):
  l=[]
  for i in range(1,int(n**0.5)+1):
    if n%i!=0:
      continue
      
    l.append([i,n//i])    
  
  return l
      
l=find_divisor_pairs(n)

ans=float("INF")

for i,j in l:
  l1_dist=(i-1)+(j-1)
  ans=min(l1_dist,ans)

print(ans)