n, a, b, c, d = map(int, input().split())
a, b, c, d = map(lambda x: x - 1, [a, b, c, d])
s = input()


def solve():
    cnt_hash = 0
    for i in range(a, max(c, d)):
        if s[i] == "#":
            cnt_hash += 1
        else:
            cnt_hash = 0

        if cnt_hash > 2:
            return False

    if c < d:
        return True

    cnt_dot = 0
    for i in range(b - 1, d + 2):
        if s[i] == ".":
            cnt_dot += 1
        else:
            cnt_dot = 0

        if cnt_dot >= 3:
            return True

    return False


print("Yes" if solve() else "No")
