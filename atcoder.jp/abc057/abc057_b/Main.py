n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]


def manhattan_dist(a, b, c, d):
    x = abs(a - c)
    y = abs(b - d)
    return x + y


for a_i, b_i in ab:
    dist = float("INF")
    nearest_point = 0
    for p, (c_j, d_j) in enumerate(cd, 1):
        dist_ij = manhattan_dist(a_i, b_i, c_j, d_j)
        if dist_ij < dist:
            nearest_point = p
            dist = dist_ij
    print(nearest_point)
