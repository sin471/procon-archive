import itertools
n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
ab2=[item[0]/item[1] for item in ab]
a,b = [list(i) for i in zip(*ab)]


x=sum(ab2)/2
l=list(itertools.accumulate(ab2))
l2=list(itertools.accumulate(a))

for i,item in enumerate(l):
    if item>=x:
        x-=l[i-1]
        ans=l2[i-1]
        ans+=ab[i][1]*x
        break
print(ans)