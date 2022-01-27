n = int(input())
h = list(map(int, input().split()))


def solve():
    for i in range(n-1, 0, -1):
        diff = h[i-1]-h[i]
        if diff >= 2:
            return False

        if diff == 1:
            h[i-1] -= 1

    return True


print("Yes" if solve() else "No")
