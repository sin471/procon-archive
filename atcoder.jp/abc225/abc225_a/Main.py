s=input()
x=len(set(s))

if x==1:
    ans=1
elif x==2:
    ans=3
else:
    ans=6
print(ans)