n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: x[1])


def solve():
    t = 0
    for a, b in ab:
        t += a
        if not t <= b:
            return False
    return True


print("Yes" if solve() else "No")
