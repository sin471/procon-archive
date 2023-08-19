from collections import defaultdict

h, w = map(int, input().split())
c = [input() for _ in range(h)]

# is_del_row = [0] * h
# is_del_col = [0] * w

row_cnts = [[0] * 26 for _ in range(h)]
col_cnts = [[0] * 26 for _ in range(w)]

acode = ord("a")
for i in range(h):
    for j in range(w):
        cij = ord(c[i][j])

        row_cnts[i][cij - acode]
        col_cnts[j][cij - acode]

        row_cnts[i][cij - acode] += 1
        col_cnts[j][cij - acode] += 1

x = y = -1
while x != 0 or y != 0:
    x = 0
    y = 0
    should_del_row = []
    for i, d in enumerate(row_cnts):
        # if is_del_row[i]:
        #     continue
        for k, v in enumerate(d):
            if v == w and v > 1:
                should_del_row.append((i, k))
                x += 1

    should_del_col = []
    for j, d in enumerate(col_cnts):
        # if is_del_col[j]:
        #     continue
        for k, v in enumerate(d):
            if v == h and v > 1:
                should_del_col.append((j, k))
                y += 1

    h -= x
    w -= y

    for i, k1 in should_del_row:
        row_cnts[i][k1] = 0
        # is_del_row[i] = 1
        for col_d in col_cnts:
            col_d[k1] -= 1

    for j, k2 in should_del_col:
        col_cnts[j][k2] = 0
        # is_del_col[j] = 1
        for row_d in row_cnts:
            row_d[k2] -= 1
print(h * w)
