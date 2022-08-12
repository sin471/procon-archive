l1,r1,l2,r2=map(int,input().split())

l=[0]*101

for i in range(l1,r1+1):
    l[i]+=1

for i in range(l2,r2+1):
    l[i]+=1

cnt=0
for i in range(101):
    if l[i]==2:
        cnt+=1
        
print(max(cnt-1,0))
