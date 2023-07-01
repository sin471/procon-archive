from functools import cmp_to_key

n = int(input())

ab = [list(map(int, input().split())) + [i] for i in range(n)]


def compare(x, y):
    a_i, b_i, i = x
    a_j, b_j, j = y
    s = a_i * (a_j + b_j)
    t = a_j * (a_i + b_i)
    return -1 if s > t or (s == t and i < j) else 1


ab.sort(key=cmp_to_key(compare))
for *_, i in ab:
    print(i + 1, end=" ")
