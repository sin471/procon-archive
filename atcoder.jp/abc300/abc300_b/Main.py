h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]


def is_same(a, b, s, t):
    for i in range(h):
        for j in range(w):
            if a[(s + i) % h][(t + j) % w] != b[i][j]:
                return False
    return True


def solve():
    for s in range(h):
        for t in range(w):
            if is_same(a, b, s, t):
                return True
    return False


print("Yes" if solve() else "No")
