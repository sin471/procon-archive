n = int(input())
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

boxes = [[] for _ in range(n + 1)]
sets = [set() for _ in range(2 * (10**5) + 1)]

for query in queries:
    if query[0] == 1:
        _, i, j = query
        boxes[j].append(i)
        sets[i].add(j)
    elif query[0] == 2:
        _, i = query
        print(*sorted(boxes[i]))
    elif query[0] == 3:
        _, i = query
        print(*sorted(sets[i]))
