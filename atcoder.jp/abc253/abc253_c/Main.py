from collections import defaultdict
from heapq import heapify, heappop, heappush

max_hq = []
min_hq = []
# heapify(max_hq)
# heapify(min_hq)
dic = defaultdict(int)


def f1(x):
    global min_hq, max_hq, dic
    heappush(min_hq, x)
    heappush(max_hq, -x)
    dic[x] += 1


def f2(x, c):
    global min_hq, max_hq, dic
    dic[x] -= min(c, dic[x])


def f3():
    global min_hq, max_hq, dic
    min_ = min_hq[0]
    max_ = max_hq[0]

    while dic[min_] == 0:
        min_ = heappop(min_hq)
        min_ = min_hq[0]

    while dic[-max_] == 0:
        max_ = heappop(max_hq)
        max_ = max_hq[0]

    print(-max_ - min_)


q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

for query in queries:
    n = query[0]
    if n == 1:
        x = query[1]
        f1(x)
    elif n == 2:
        x, c = query[1], query[2]
        f2(x, c)
    elif n == 3:
        f3()
