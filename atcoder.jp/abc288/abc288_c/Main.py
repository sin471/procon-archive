n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

parent = list(range(n))

def root(x):
    if parent[x] == x:
        return x

    parent[x] = root(parent[x])
    return parent[x]


def unite(x, y):
    root_x = root(x)
    root_y = root(y)
    if root_x == root_y:
        return 

    parent[root_y] = root(x)


def same(x, y):
    return root(x) == root(y)


for a_i, b_i in ab:
    unite(a_i - 1, b_i - 1)

component_cnt = 0
for i, parent_i in enumerate(parent):
    if parent_i == i:
        component_cnt += 1

print(m - n + component_cnt)
