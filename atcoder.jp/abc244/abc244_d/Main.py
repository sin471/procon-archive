def solve():
    s = "".join(input().split())
    t = "".join(input().split())
    if s == t:
        return True

    for i in range(3):
        if s[i] == t[i]:
            return False

    return True


print("Yes" if solve() else "No")
