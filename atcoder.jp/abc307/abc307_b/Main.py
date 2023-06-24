n = int(input())
s = [input() for _ in range(n)]


def is_kaibun(s):
    return s == s[::-1]


def solve():
    for i in range(n):
        for j in range(n):
            if i != j and is_kaibun(s[i] + s[j]):
                return True
    return False


print("Yes" if solve() else "No")
