import sys

# import pypyjit
# pypyjit.set_param("max_unroll_recursion=0")
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]
n = H * W
parents = list(range(n + 1))
size = [1] * (n + 1)


def root(v):
    if parents[v] == v:
        return v

    r = root(parents[v])
    parents[v] = r
    return r


def unite(u, v):
    ru = root(u)
    rv = root(v)
    if ru == rv:
        return

    if size[ru] <= size[rv]:
        parents[ru] = rv
        size[ru] += size[rv]
    else:
        parents[rv] = ru
        size[rv] += size[ru]


def same(u, v):
    return root(u) == root(v)


def is_inside(x, y, h, w):
    return 0 <= x < h and 0 <= y < w


is_red = [[0] * W for _ in range(H)]

for q in queries:
    if q[0] == 1:
        _, r, c = q
        r -= 1
        c -= 1

        is_red[r][c] = 1

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if not is_inside(r + dx, c + dy, H, W):
                continue

            if is_red[r + dx][c + dy]:
                u = r * W + c
                v = (r + dx) * W + (c + dy)
                unite(u, v)

    else:
        _, ra, ca, rb, cb = q
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1

        if same(ra * W + ca, rb * W + cb) and is_red[ra][ca] and is_red[rb][cb]:
            print("Yes")
        else:
            print("No")
