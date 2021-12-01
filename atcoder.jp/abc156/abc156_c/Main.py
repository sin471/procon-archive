n = int(input())
x = list(map(int,input().split()))

ans=float("Inf")
x.sort()

for p in range(x[0],x[-1]+1):
    sum_=sum(map(lambda xi:(xi-p)**2,x))
    ans=min(ans,sum_)

print(ans)
