mod=10**9+7
n=int(input())

power=1
for i in range(1,n+1):
    power*=i
    power%=mod

print(power)