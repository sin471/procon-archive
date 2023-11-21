n, q = map(int, input().split())
c = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

boxes = [{c[i]} for i in range(n)]

for a, b in queries:
    if len(boxes[a - 1]) < len(boxes[b - 1]):
        boxes[b - 1].update(boxes[a - 1])
    else:
        boxes[a - 1].update(boxes[b - 1])
        boxes[b - 1] = boxes[a - 1]

    boxes[a - 1] = set()
    print(len(boxes[b - 1]))
