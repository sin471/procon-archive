from collections import Counter
n=int(input())
a=list(map(int,input().split()))

c=Counter(a)

for i in c.items():
  if i[1]!=4:
    print(i[0])
    break