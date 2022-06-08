n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

max_a=max(a)

is_good=[1]*n
for i in range(k):
    is_good[b[i]-1]=0

for i in range(n):
    if (not is_good[i]) and a[i]==max_a:
        print("Yes")
        break
else:
    print("No")

