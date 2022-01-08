import string
s = input()


def solve():
    if s[0] != "A":
        return False

    if s[2:-1].count("C") != 1:
        return False

    l = [i for i in s if i in string.ascii_uppercase]

    if len(l) != 2:
        return False

    return True


print("AC" if solve() else "WA")
