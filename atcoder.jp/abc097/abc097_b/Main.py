x=int(input())

ans=1
for b in range(1,x):
  for p in range(2,x):
    a=b**p
    if a>x:
      break
    ans=max(a,ans)

print(ans)