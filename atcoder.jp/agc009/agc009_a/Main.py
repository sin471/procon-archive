from math import ceil

n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]

s=0
for i in range(n-1,-1,-1):
    a_i,b_i = ab[i]
    a_i+=s
    s+=(-a_i)%b_i

print(s)
