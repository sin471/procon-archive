n=int(input())
a=list(map(int,input().split()))

factor_2_cnt=0

for i in a:
  while i%2==0:
    i//=2
    factor_2_cnt+=1

print(factor_2_cnt)