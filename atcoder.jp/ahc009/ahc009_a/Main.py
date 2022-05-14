from typing import List, Dict

# LiteralはPypyで使えないので使用禁止
from collections import deque

field_type = List[List[int]]
point_type = List[int]
point_dist_type = List[int]


def my_input():
    l = input().split()

    field_h: field_type = [list(map(int, list(input()))) for _ in range(20)]
    field_v: field_type = [list(map(int, list(input()))) for _ in range(19)]

    return (int(l[0]), int(l[1]), int(l[2]), int(l[3]), float(l[4]), field_h, field_v)


si, sj, ti, tj, p, field_h, field_v = my_input()
commands = ("U", "D", "L", "R")


def is_inside_field(next_x: int, next_y: int):
    if 0 <= next_x < 20 and 0 <= next_y < 20:
        return True
    else:
        return False


def can_move(command: str, now: point_type):
    x, y = now
    next_x, next_y = command_to_coordinate(command, now)

    if not is_inside_field(next_x, next_y):
        return False
    if command == "U" and not field_v[x - 1][y]:
        return True
    if command == "D" and not field_v[x][y]:
        return True
    if command == "L" and not field_h[x][y - 1]:
        return True
    if command == "R" and not field_h[x][y]:
        return True
    return False


def command_to_coordinate(command: str, now: List[int]):
    x, y = now
    commands_dict: Dict[str, point_dist_type] = {
        "U": [-1, 0],
        "D": [1, 0],
        "L": [0, -1],
        "R": [0, 1],
    }

    dx, dy = commands_dict[command]
    return [x + dx, y + dy]


def step_bfs(start: point_type, goal: point_type):
    step_field = [[-1] * 20 for _ in range(20)]
    q: deque[List[int]] = deque()

    q.append(start)
    step_field[start[0]][start[1]] = 0

    while len(q):
        now = q.popleft()

        for command in commands:
            if not can_move(command, now):
                continue

            next_x, next_y = command_to_coordinate(command, now)
            if step_field[next_x][next_y] != -1:
                continue

            q.append([next_x, next_y])
            now_step = step_field[now[0]][now[1]]
            step_field[next_x][next_y] = now_step + 1

            # goalのステップ数が見つかった時点で打ち切る
            if [next_x, next_y] == goal:
                return step_field

    return step_field


def create_commands_by_stepfield(step_field: List[List[int]], goal: point_type):
    now = goal
    now_x, now_y = now
    now_step = step_field[now_x][now_y]
    goal_to_start_commands: List[str] = []

    while now_step != 0:
        for command in commands:
            next_x, next_y = command_to_coordinate(command, now)
            now_step = step_field[now_x][now_y]

            # 2 3
            #  -
            # 3 4
            # のような場合右→下と下→右の移動の区別ができないので、壁があるかをもう一度判定する
            if not can_move(command, now):
                continue
            next_step = step_field[next_x][next_y]

            # 逆算なので、次の方が小さくなるようにする
            if now_step - next_step == 1:
                goal_to_start_commands.append(command)
                now_x, now_y = next_x, next_y
                now = [now_x, now_y]
                break

    start_to_goal_commands: List[str] = reverse_commands(goal_to_start_commands)
    return start_to_goal_commands


def reverse_commands(commands: List[str]):
    commands_dict = {"U": "D", "D": "U", "L": "R", "R": "L"}
    reversed_commands = [commands_dict[command] for command in commands][::-1]
    return reversed_commands


def print_formatted_2dlist(list_2d: List[List[int]]):
    for list_ in list_2d:
        print(list(map(lambda x: str(x).zfill(3), list_)))


def main():
    start = [si, sj]
    goal = [ti, tj]
    step_field = step_bfs(start, goal)
    start_to_goal_commands = create_commands_by_stepfield(step_field, goal)
    print("".join(start_to_goal_commands)+((200-len(start_to_goal_commands))//2)*"DR")
    


main()
