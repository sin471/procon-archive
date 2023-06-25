from copy import deepcopy

Ha, Wa = map(int, input().split())
A = [list(input()) for _ in range(Ha)]
Hb, Wb = map(int, input().split())
B = [list(input()) for _ in range(Hb)]
Hx, Wx = map(int, input().split())
X = [list(input()) for _ in range(Hx)]


def cnt(ll, char):
    return sum(ll[i].count(char) for i in range(len(ll)))


def vec(ll, h, w):
    vecs = []
    is_first = True
    x, y = 0, 0
    for i in range(h):
        for j in range(w):
            if ll[i][j] != "#":
                continue

            if is_first:
                x, y = i, j
                is_first = False

            vecs.append((i - x, j - y))
    return vecs


def is_insideX(x, y):
    return 0 <= x < Hx and 0 <= y < Wx


def replace_sharp(X, x, y, vecs):
    X = deepcopy(X)
    for dx, dy in vecs:
        if is_insideX(x + dx, y + dy) and X[x + dx][y + dy] != ".":
            X[x + dx][y + dy] = "O"
        else:
            return X, False
    return X, True


def coordinate(ll, h, w, char):
    l = []
    for i in range(h):
        for j in range(w):
            if ll[i][j] == char:
                l.append((i, j))
    return l


def exist(X, char):
    return any(char in X_i for X_i in X)


def solve():
    vec_a = vec(A, Ha, Wa)
    vec_b = vec(B, Hb, Wb)
    x_sharps = coordinate(X, Hx, Wx, "#")
    cnt_sharpX = cnt(X, "#")
    for i1, j1 in x_sharps:
        AandX, has_succeeded = replace_sharp(X, i1, j1, vec_a)
        if not has_succeeded:
            continue
        for i2, j2 in x_sharps:
            ABandX, has_succeeded = replace_sharp(AandX, i2, j2, vec_b)
            if not has_succeeded:
                continue

            if not exist(ABandX, "#") and cnt(ABandX, "O") == cnt_sharpX:
                return True
    return False


print("Yes" if solve() else "No")
