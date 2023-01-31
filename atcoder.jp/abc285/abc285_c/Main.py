s=reversed(input())

n=0
for i,s_i in enumerate(s):
    n+=(26**i)*(ord(s_i)-64)

print(n)
