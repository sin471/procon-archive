s=input()
a,z=0,0

n=len(s)
for i in range(n):
    if s[i]=="A":
        a=i+1
        break

for i in range(n-1,-1,-1):
    if s[i]=="Z":
        z=i+1
        break

print(z-(a-1))