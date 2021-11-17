n=int(input())
s=list(map(int,input().split()))

ans=len(s)

for si in s:
    flag=False
    for a in range(1,si+1):
      #formula=4*a*b+3*a+3*b
      b=(si-3*a)/(4*a+3)
      if b.is_integer() and b>0:
        ans-=1
        break

print(ans)