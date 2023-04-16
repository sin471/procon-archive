from copy import deepcopy

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]


def solve():
    global a
    for _ in range(4):
        flag = False
        for i in range(n):
            if flag:
                break
            for j in range(n):
                if a[i][j] and not b[i][j]:
                    flag = True
                    break
        else:
            return True

        a2 = deepcopy(a)
        for i in range(n):
            for j in range(n):
                a[i][j] = a2[n - j - 1][i]

    return False


print("Yes" if solve() else "No")
