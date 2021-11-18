s,t=map(int,input().split())
cnt=0
for a in range(101):
  for b in range(s-a+1):
    for c in range(s-(a+b)+1):
        sum_abc=a+b+c
        product_abc=a*b*c
        if sum_abc<=s and product_abc<=t:
          cnt+=1

print(cnt)