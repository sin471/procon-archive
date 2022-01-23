n,m=map(int,input().split())
s=set(input().split())
t=set(input().split())

for i in s:
  print("Yes" if i in t else "No")