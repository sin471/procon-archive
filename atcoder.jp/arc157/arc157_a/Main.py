n, a, b, c, d = map(int, input().split())


def solve():
    if b == c == 0 and a != 0 and d != 0:
        return False

    if abs(b - c) >= 2:
        return False

    return True


print("Yes" if solve() else "No")
