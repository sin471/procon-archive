n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]


def extract_3x3(a, center):
    x, y = center
    outer_list = []
    for dx in [-1, 0, 1]:
        inner_list = []
        for dy in [-1, 0, 1]:
            inner_list.append(a[(x + dx) % n][(y + dy) % n])

        outer_list.append(inner_list)
    return outer_list


def around_max_directions(x, y):
    a_3x3 = extract_3x3(a, [x, y])
    a_3x3[1][1] = float("-INF")
    m = max(map(lambda x: max(x), a_3x3))

    result_list = []
    for i in range(3):
        for j in range(3):
            if a_3x3[i][j] == m:
                result_list.append([i - 1, j - 1])

    return result_list


def join_int(l):
    return int("".join(map(str, l)))


max_a = max(map(lambda x: max(x), a))
max_a_indexes = []
for i in range(n):
    for j in range(n):
        if a[i][j] == max_a:
            max_a_indexes.append([i, j])


outer_list = []
for start_x, start_y in max_a_indexes:
    mid_list = []

    for dx, dy in around_max_directions(start_x, start_y):
        x, y = start_x, start_y

        inner_list = []
        inner_list.append(a[x][y])

        for _ in range(n - 1):
            x += dx
            y += dy

            inner_list.append(a[x % n][y % n])

        mid_list.append(join_int(inner_list))

    outer_list.append(max(mid_list))

print(max(outer_list))
