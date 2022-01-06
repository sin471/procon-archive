n=int(input())
a=[int(input()) for i in range(n)]
sorted_a=sorted(a,reverse=True)

maximum_1=sorted_a[0]
maximum_2=sorted_a[1]

for i in a:
  if i==maximum_1:
    print(maximum_2)
  else:
    print(maximum_1)