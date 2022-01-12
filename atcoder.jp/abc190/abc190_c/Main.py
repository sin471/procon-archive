n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(m)]
k=int(input())
cd=[list(map(int,input().split())) for i in range(k)]

ans=float("-inf")

for bit in range(1<<k):
  put_c=[]
  put_d=[]
  balls=[0]*n
  cnt=0
  for i in range(k):
    if bit&(1<<i):
      put_c.append(i)
    else:
      put_d.append(i)

  for j in put_c:
    balls[cd[j][0]-1]=1

  for j in put_d:
    balls[cd[j][1]-1]=1

  for ai,bi in ab:
    if balls[ai-1] and balls[bi-1]:
      cnt+=1

  ans=max(ans,cnt)
print(ans)