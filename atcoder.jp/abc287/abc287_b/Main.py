n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]


def f(s_i):
    for t_j in t:
        if s_i[-3:] == t_j:
            return 1
    return 0


cnt = 0
for s_i in s:
    cnt += f(s_i)

print(cnt)
