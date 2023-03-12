import sys
sys.setrecursionlimit(10**7)

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

path = list()
ans = 0


def dfs(x, y):
    global ans

    a_xy = a[x][y]
    d = [[1, 0], [0, 1]]

    if a_xy in path:
        return
    path.append(a_xy)

    if (x, y) == (h - 1, w - 1):
        ans += 1

    else:
        for dx, dy in d:
            if x + dx >= h or y + dy >= w:
                continue
            dfs(x + dx, y + dy)
    
    path.remove(a_xy)


dfs(0, 0)
print(ans)
