n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def solve():
    for i in b:
        try:
            a.pop(a.index(i))
        except ValueError:
            return False
    return True


print("Yes" if solve() else "No")
