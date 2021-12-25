import itertools
import operator

# sys.setrecursionlimit(10**5)
n, x = map(int, input().split())

L, A = [], []
cnt = 0
for i in range(n):
    l, *a = map(int, input().split())
    L.append(l)
    A.append(a)


def prod(a):
    ans = 1
    for ai in a:
        ans *= ai
    return ans


def dfs(seki, i):
    global cnt
    if i == n:
        if seki == x:
            cnt += 1
        return
    for c in A[i]:
        if i+1 <= n:
            seki *= c
            dfs(seki, i+1)
            seki //= c


seki = 1
i = 0
dfs(seki, i)
print(cnt)
