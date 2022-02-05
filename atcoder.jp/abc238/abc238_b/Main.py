from itertools import accumulate

n=int(input())
a=list(map(int,input().split()))

l=list(accumulate(a))
b=[]

for i in l:
    b.append(i%360)

b.sort()

ans=max(360-b[-1],b[0])

for i in range(1,n):
    diff=b[i]-b[i-1]
    ans=max(ans,diff)

print(ans)
