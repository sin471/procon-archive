n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]


def find_dist(x1, y1, x2, y2):
    tmp = (x1-x2)**2+(y1-y2)**2
    return tmp**0.5


ans = float("-INF")
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = xy[i][0], xy[i][1]
        x2, y2 = xy[j][0], xy[j][1]
        dist = find_dist(x1, y1, x2, y2)
        ans = max(dist, ans)

print(ans)
