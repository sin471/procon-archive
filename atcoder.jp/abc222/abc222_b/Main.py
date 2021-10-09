N,P=map(int,input().split())
a=list(map(int,input().split()))
b=[i for i in a if i<P]
print(len(b))
