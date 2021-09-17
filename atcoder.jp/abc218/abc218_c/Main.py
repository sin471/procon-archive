import sys

N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]


def index_sharps(shape):
    return [(n, m) for n, i in enumerate(shape)for m, j in enumerate(i) if j == '#']


s_index = index_sharps(S)
t_index = index_sharps(T)


def translate_to_origin(l_shape):
    criteria_value = l_shape[0]
    return [list(map(lambda x, y:x-y, i, criteria_value)) for i in l_shape]


def turn_to_clockwise_per_90_degree(l_shape):
    # 左から順に、時計回りにに90°,180°,270°,360°回転
    return [[(j, -i) for i, j in l_shape], [(-i, -j) for i, j in l_shape],
            [(-j, i) for i, j in l_shape], l_shape]


turned_s = turn_to_clockwise_per_90_degree(s_index)
turned_s = list(map(sorted, turned_s))

translated_t = translate_to_origin(t_index)

turned_and_translated_s = list(map(translate_to_origin, turned_s))

for translated_s in turned_and_translated_s:
    if translated_s == translated_t:
        print("Yes")
        sys.exit()
else:
    print("No")
