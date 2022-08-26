import sys

sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
p_a_b = [list(map(int, input().split())) for _ in range(q)]


class Union_find:
    def __init__(self, n):
        self.graph = list(range(n))

    def root(self, x):
        if self.graph[x] != x:
            r = self.root(self.graph[x])
            self.graph[x] = r
        return self.graph[x]

    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        self.graph[rb] = ra


graph = Union_find(n)

for p, a, b in p_a_b:
    if p == 0:
        graph.unite(a, b)
    elif p == 1:
        is_connected = graph.root(a) == graph.root(b)
        print("Yes" if is_connected else "No")
