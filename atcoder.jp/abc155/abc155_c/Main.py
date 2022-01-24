from collections import Counter

n=int(input())
s=[input() for i in range(n)]

c=Counter(s)

c_most= c.most_common()
maximum=c_most[0][1]
l=[]
for i in c_most:
    if i[1]!=maximum:
        break
    else:
         l.append(i[0])

print(*sorted(l),sep="\n")