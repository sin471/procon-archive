n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

from_ = set()
to = set()

for a, b in ab:
    if a == 1:
        to.add(b)
    if b == n:
        from_.add(a)

print("POSSIBLE" if from_ & to else "IMPOSSIBLE")
