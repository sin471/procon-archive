import sys
sys.setrecursionlimit(10**6)

n = int(input())
cp = []
for _ in range(n):
    c, *p = list(map(int, input().split()))
    cp.append([c, *p])

has_read = [0] * n

ans = []


def dfs(i):
    global has_read
    global ans
    c, *pi = cp[i - 1]

    for pij in pi:
        if has_read[pij - 1]:
            continue
        dfs(pij)
        has_read[pij - 1] = 1
        ans.append(pij)


dfs(1)
print(*ans)
