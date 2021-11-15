R,G,B,N=map(int,input().split())
cnt=0
for r in range(N//R+1):
  for g in range(N//G+1):
    rg_balls=(R*r+G*g)
    if (N-rg_balls)%B==0 and  N>=rg_balls:
      cnt+=1

print(cnt)