n=int(input())
digits_xx=n%100

bought=0
for i in range(5,0,-1):
  bought+=digits_xx//i
  digits_xx%=i


print(1 if bought*100 <= n else 0)