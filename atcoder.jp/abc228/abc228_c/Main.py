n,k=map(int,input().split())
p=[sum(map(int,input().split())) for _ in range(n)]

p2=sorted(p,reverse=True)

flags=["No"]*n

p2_rank_k=p2[k-1]

for i in range(n):
  if p[i]+300 >= p2_rank_k:
    flags[i]="Yes"


print(*flags,sep="\n")