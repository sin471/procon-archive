import collections

q = int(input())
querys = [list(map(int, input().split())) for _ in range(q)]


def query1(x, c, deque):
    deque.append([x, c])


def query2(c, deque):
    sum_num_of_balls = 0
    result = 0

    x = -1
    while sum_num_of_balls < c:
        ball = deque.popleft()
        x, num_of_balls = ball[0], ball[1]
        sum_num_of_balls += num_of_balls
        result += x*num_of_balls

    # 取り過ぎたら戻す
    if sum_num_of_balls > c:
        deque.appendleft([x, sum_num_of_balls-c])
        result -= x*(sum_num_of_balls-c)

    return result


deque = collections.deque()
for query in querys:
    if query[0] == 1:
        _, x, c = query
        query1(x, c, deque)

    elif query[0] == 2:
        _, c = query
        print(query2(c, deque))