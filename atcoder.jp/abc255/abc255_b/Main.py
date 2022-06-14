n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]


def dist(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


ans = -1
INF = float("INF")
l = [INF]
for xy_i in xy:
    d = INF
    for a_j in a:
        xy_aj = xy[a_j - 1]
        d = min(dist(xy_i, xy_aj), d)
    ans = max(d, ans)

print(ans)
