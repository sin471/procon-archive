n = int(input())
a = list(map(int, input().split()))


def solve(n, a):
    d = dict()
    d[1] = d[2] = d[4] = 0

    for a_i in a:
        if a_i % 4 == 0:
            d[4] += 1
        elif a_i % 2 == 0:
            d[2] += 1
        else:
            d[1] += 1

    if d[1] <= d[4] + 1 and d[2] == 0:
        return True
    elif d[1] <= d[4] and d[2] >= 1:
        return True
    else:
        return False


print("Yes" if solve(n, a) else "No")
