from collections import deque
from typing import List, Tuple

BALLSUM = 30 * 31 // 2


def input_():
    ball_positions: List[Tuple[int, int]] = [(-1, -1)] * BALLSUM
    ll = [list(map(int, input().split())) for _ in range(30)]
    for i, l in enumerate(ll):
        for j in range(i + 1):
            ball_positions[l[j]] = (i, j)

    return ball_positions, ll


# ball_positions[id]=(idealx,y)
# ids[idealx][y]= ball_id

ball_positions, ids = input_()
# もう動かさないball=1
locked = [0] * BALLSUM


def swap(id1, id2):
    global ball_positions
    global ids
    global ans

    (x1, y1), (x2, y2) = ball_positions[id1], ball_positions[id2]

    ball_positions[id1], ball_positions[id2] = (x2, y2), (x1, y1)

    ids[x1][y1], ids[x2][y2] = id2, id1
    ans.append([(x1, y1), (x2, y2)])


def is_inside(idealx, y):
    return 0 <= idealx < 30 and 0 <= y < idealx + 1


def can_swap(xy1, xy2):
    (x1, y1), (x2, y2) = xy1, xy2
    return (
        is_inside(*xy1)
        and is_inside(*xy2)
        and not (locked[ids[x1][y1]] or locked[ids[x2][y2]])
    )


def move(id1, command):
    idealx, y = ball_positions[id1]
    d = {"R": [[0, 1]], "U": [[-1, 0], [-1, -1]], "L": [[0, -1]]}
    for dx, dy in d[command]:
        if can_swap((idealx, y), (idealx + dx, y + dy)):
            swap(id1, ids[idealx + dx][y + dy])
        else:
            continue
        break


def ideal_x(id_):
    # 一時的に1indexedで考える
    id_ += 1
    for idealx in range(1, 31):
        if (idealx - 1) * idealx // 2 < id_ <= (idealx + 1) * idealx // 2:
            return idealx - 1
    return -1


# seen = [[-1] * i for i in range(1, 31)]


# def shortest_command_bfs(xy, ideal_x):
#     global commands
#     commands = []
#     dist = 0
#     q = deque()
#     q.append(xy)
#     while q:
#         idealx, y = q.pop()
#         seen[idealx][y] = dist
#         for dx, dy in [[-1, 0], [-1, -1], [0, 1], [0, -1]]:
#             if not is_inside(idealx + dx, y + dy) or seen[idealx + dx][y + dy] != -1:
#                 continue
#             q.appendleft((idealx + dx, y + dy))
#         dist = seen[idealx][y] + 1

#         # shortest_command_bfs(idealx + dx, y + dy, ideal_x)
#     print(seen)


# print(shortest_command_bfs(ball_positions[0], 0))
swap_cnt = 0
swap_max = 10000
ans = []

for id_ in range(BALLSUM):
    idealx = ideal_x(id_)
    if swap_cnt >= swap_max:
        break
    r_move_cnt = 0
    while ball_positions[id_][0] > idealx and swap_cnt < swap_max:
        x1, y1 = ball_positions[id_]
        width = x1 + 1
        if can_swap((x1, y1), (x1 - 1, y1)) or can_swap((x1, y1), (x1 - 1, y1 - 1)):
            move(id_, "U")
        elif width > r_move_cnt:
            r_move_cnt += 1
            move(id_, "R")
        else:
            move(id_, "L")
        swap_cnt += 1

    locked[id_] = 1


def output(ans):
    print(len(ans))
    for xy1, xy2 in ans:
        print(*xy1, *xy2)


output(ans)
