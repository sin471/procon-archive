n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()


def solve():
    l = 0
    r = 0
    while l < n:
        while r < n:
            d = a[r] - a[l]
            if d == x or -d == x:
                return True
            elif d > x:
                break
            r += 1
        l += 1

    return False


print("Yes" if solve() else "No")
