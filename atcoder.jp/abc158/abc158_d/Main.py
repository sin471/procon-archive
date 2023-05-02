from collections import deque

s = deque(input())
q = int(input())
queries = [input().split() for _ in range(q)]

is_reversed = False
for query in queries:
    if query[0] == "1":
        is_reversed = not is_reversed
    elif query[0] == "2":
        f, c = int(query[1]), query[2]
        if is_reversed:
            f += 1

        if f % 2 == 1:
            s.appendleft(c)
        elif f % 2 == 0:
            s.append(c)

string = "".join(s)
print(string[::-1] if is_reversed else string)
