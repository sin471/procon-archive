n,k=map(int,input().split())

dice=1/n
coin=1/2
p=[]
for i in range(1,n+1):
    j=0
    while i*(2**j)<k:
        j+=1
    p.append(dice*(coin**j))

print(sum(p))
    