from collections import defaultdict


def solve():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    s = input()

    right_min = dict()
    left_max = dict()
    inf = float("INF")
    minus_inf = float("-INF")

    for i in range(n):
        x_i, y_i = xy[i]
        s_i = s[i]
        if s_i == "L":
            left_max[y_i] = max(left_max.get(y_i, minus_inf), x_i)
        else:
            right_min[y_i] = min(right_min.get(y_i, inf), x_i)

    for i in range(n):
        x_i, y_i = xy[i]
        s_i = s[i]
        if s_i == "R":
            if x_i < left_max.get(y_i, minus_inf):
                return True
        else:
            if right_min.get(y_i, inf) < x_i:
                return True
    return False


print("Yes" if solve() else "No")

#y_i==y_j & s_i!=s_j & 背中合わせでない
