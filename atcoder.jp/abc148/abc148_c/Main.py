def gcd(a,b):
  r=a%b
  if r==0:
    return b
  a,b=b,r
  return gcd(a,b)

  
def lcm(a,b,g):
  return a*b//g

a,b=map(int,input().split())
g=gcd(a,b)
print(lcm(a,b,g))