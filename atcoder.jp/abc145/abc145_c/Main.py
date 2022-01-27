from itertools import permutations
from math import factorial
n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]

p=permutations(xy)

l=[]
for p_i in p:
    dist=0
    for i in range(1,n):
        dist+=((p_i[i-1][0]-p_i[i][0])**2+(p_i[i-1][1]-p_i[i][1])**2)**0.5
    l.append(dist)

print(sum(l)/factorial(n))