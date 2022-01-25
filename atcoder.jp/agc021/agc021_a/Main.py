n=list(input())

m=sum(map(int,n))

n[0]=int(n[0])-1

l=[n[0]]+([9]*(len(n)-1))

print(max(sum(l),m))