n,k,a=map(int,input().split())
ans=(a+k-1)%n
if ans:print(ans)
else:print(n)