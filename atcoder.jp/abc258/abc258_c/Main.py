n, q = map(int, input().split())
s = input()
queries = [list(map(int, input().split())) for _ in range(q)]


def q1(x, head):
    return (head + x) % n


def q2(x, head):
    print(s[(x - 1) - head])


head = 0

for t, x in queries:
    if t == 1:
        head = q1(x, head)
    else:
        q2(x, head)
