s = input()
n = int(input())


def solve():
    min_ = max_ = 0
    table2 = [0] * 60
    table2[0] = 1
    for i in range(1, 60):
        table2[i] = table2[i - 1] * 2

    for tmp, char in enumerate(s):
        i = len(s) - 1 - tmp
        if char == "1":
            min_ += table2[i]
            max_ += table2[i]
        elif char == "?":
            max_ += table2[i]

    if min_ > n:
        return -1
    m = min_
    for tmp, char in enumerate(s):
        i = len(s) - 1 - tmp
        if char == "?":
            if m + table2[i] <= n:
                m += table2[i]

    return m


print(solve())
