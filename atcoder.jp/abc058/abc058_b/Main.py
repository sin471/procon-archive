o = input()
e = input()

l=[]
last=""
if len(o)!=len(e):
  last=max(o,e,key=len)[-1]

for i,j in zip(o,e):
  l.append(i)
  l.append(j)
l.append(last)
print("".join(l))
