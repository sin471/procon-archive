n, m = map(int, input().split())

ans = 0
if n >= 2 and m >= 2:
    ans = (n - 2) * (m - 2)
elif n == 1 and m == 1:
    ans = 1
elif n == 1 or m == 1:
    ans = max(n - 2, m - 2)

print(ans)
