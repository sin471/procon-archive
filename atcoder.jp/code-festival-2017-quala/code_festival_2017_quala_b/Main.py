n, m, k = map(int, input().split())


def solve():
    for x in range(n + 1):
        for y in range(m + 1):
            if y * (n - x) + x * (m - y) == k:
                return True
    return False


print("Yes" if solve() else "No")
