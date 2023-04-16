from collections import deque

q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
s = deque([1])
t = 1
mod = 998244353

for query in queries:
    if query[0] == 1:
        _, x = query
        s.append(x)
        t = (10 * t + x) % mod

    elif query[0] == 2:
        exp = len(s) - 1
        head = s.popleft()
        t -= head * pow(10, exp, mod)
        t %= mod

    elif query[0] == 3:
        print(t)
