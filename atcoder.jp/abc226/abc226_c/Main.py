import sys

sys.setrecursionlimit(10**8)

n = int(input())
tka = [list(map(int, input().split())) for _ in range(n)]

t=0

flag_list=[False]*n

def saiki(n):
    global t
    global flag_list
    a_i=tka[n-1][2:]
    for i in a_i:
        if not flag_list[n-1]:
            saiki(i)
    if not flag_list[n-1]:
        t+=tka[n-1][0]
        flag_list[n-1]=True
    return t

print(saiki(n))