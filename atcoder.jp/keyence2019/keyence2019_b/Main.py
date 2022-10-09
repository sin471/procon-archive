s = input()


def solve():
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            s2 = s[:i] + s[j:]

            if s2 == "keyence":
                return True
    return False


print("YES" if solve() else "NO")
