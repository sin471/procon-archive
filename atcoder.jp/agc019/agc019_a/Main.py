q,h,s,d=map(int,input().split())
n=int(input())

double=[min(q*8,h*4,s*2,d),2]
single= [min(q*4,h*2,s),1]


sizes=[double,single]

ans=0

for price,size in sizes:
  ans+=(n//size)*price
  n%=size
  
  
print(int(ans))
  