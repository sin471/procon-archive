N=int(input())
p=list(map(int,input().split()))

q=[None]*N
for i,pi in enumerate(p,1):
    q[pi-1]=i

q=map(str,q)
print(" ".join(q))