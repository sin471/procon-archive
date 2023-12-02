n, s, m, l = map(int, input().split())
ans = float("INF")
for i in range(n+1):
    for j in range(n + 1):
        for k in range(n + 1):
            if i * 6 + j * 8 + k * 12 >= n:
                x = s * i + m * j + l * k
                ans = min(ans, x)

print(ans)
