n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

ul = [list("###."), list("###."), list("###."), list("....")]
lr = [
    list("...."),
    list(".###"),
    list(".###"),
    list(".###"),
]


def judge(i, j):
    if i + 8 >= n or j + 8 >= m:
        return False

    for i2 in range(4):
        for j2 in range(4):
            if s[i + i2][j + j2] != ul[i2][j2]:
                return False

    for i2 in range(4):
        for j2 in range(4):
            if s[i + i2 + 5][j + j2 + 5] != lr[i2][j2]:
                return False
    return True


ans = []
for i in range(n):
    for j in range(m):
        if judge(i, j):
            ans.append((i, j))

for i, j in ans:
    print(i + 1, j + 1)
