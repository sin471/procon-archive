n=int(input())
a=list(map(int,input().split()))

delete=a[0]
for i in range(n):
    if delete<a[i]:
        delete=a[i]
    
    if a[i]<delete:
        break

for i in a:
    if i!=delete:
        print(i,end=" ")
