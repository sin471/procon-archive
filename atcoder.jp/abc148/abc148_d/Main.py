n=int(input())
a=list(map(int,input().split()))

crushed=0
m=1
for ai in a:
    if ai==m:
        m+=1
    else:
        crushed+=1
      
print(crushed if crushed!=n else -1)
      
      