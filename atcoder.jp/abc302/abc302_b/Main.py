h, w = map(int, input().split())
s = [input() for _ in range(h)]

string = "snuke"
d = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]


def search_straight(i, j, dx, dy):
    cnt = 0
    l = []
    is_inner = True
    while is_inner and s[i][j] == string[cnt]:
        cnt += 1
        l.append([i + 1, j + 1])
        if cnt == 5:
            return l
        i += dx
        j += dy
        is_inner = 0 <= i < h and 0 <= j < w
    return l


def solve():
    for i in range(h):
        for j in range(w):
            if s[i][j] == "s":
                for dx, dy in d:
                    l = search_straight(i, j, dx, dy)
                    if len(l) == 5:
                        return l


for i, j in solve():
    print(i, j)
