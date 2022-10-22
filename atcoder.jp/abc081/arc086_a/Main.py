n,k=map(int,input().split())
a=list(map(int,input().split()))
d=dict()

for a_i in a:
    d.setdefault(a_i,0)
    d[a_i]+=1

sorted_values=sorted(d.values())
print(sum(sorted_values[:len(d)-k]))
