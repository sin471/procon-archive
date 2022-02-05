n = int(input())
digit = len(str(n))


def sum_to_a(a):
    return a*(a+1)//2


mod = 998244353
ans = 0

for i in range(digit-1):
    a = 10**(i+1)-10**i
    ans += sum_to_a(a)

x = n-(10**(digit-1))+1

ans += sum_to_a(x) 

print(ans%mod)
