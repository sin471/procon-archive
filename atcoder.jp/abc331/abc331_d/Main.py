n, q = map(int, input().split())
p = [list(input()) for _ in range(n)]
queries = [list(map(int, input().split())) for _ in range(q)]

s = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        b = 1 if p[i][j] == "B" else 0

        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + b


def f(a, b):
    if a < 0 or b < 0:
        return 0

    p_cnt = ((a + 1) // n) * ((b + 1) // n)

    x = ((a + 1) // n) * s[n][(b + 1) % n]
    y = ((b + 1) // n) * s[(a + 1) % n][n]
    z = s[(a + 1) % n][(b + 1) % n]

    res = p_cnt * s[-1][-1] + x + y + z
    return res

for a, b, c, d in queries:
    ans = f(c, d) - f(a - 1, d) - f(c, b - 1) + f(a - 1, b - 1)
    print(ans)
