n=int(input())

x=len(bin(n)[2:])-1
print(n&1<<x)