c = [list(map(int, input().split())) for _ in range(3)]


def solve():
    for i in range(1, 3):
        d = []
        for j in range(3):
            d.append(c[i][j] - c[i - 1][j])

        if len(set(d)) == 1:
            pass
        else:
            return False
    return True


print("Yes" if solve() else "No")
