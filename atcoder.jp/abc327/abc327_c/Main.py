a = [list(map(int, input().split())) for _ in range(9)]

s = set(range(1, 10))


def solve():
    if not all(set(ai) == s for ai in a):
        return False

    if not all(set(ai) == s for ai in zip(*a)):
        return False

    for i1 in range(3):
        for j1 in range(3):
            l1 = []
            for i in range(3):
                for j in range(3):
                    l1.append(a[i + 3 * i1][j + 3 * j1])
            if not set(l1) == s:
                return False

    return True


print("Yes" if solve() else "No")
