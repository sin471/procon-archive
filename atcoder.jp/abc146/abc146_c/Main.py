a, b, x = map(int, input().split())

# AN+Bd<=X
# N<=(X-Bd)/A
ans = 0
for d in range(1, 11):
    can_buy = min((x - b * d) // a, 10**9)
    if 10 ** (d - 1) <= can_buy < 10**d:
        ans = max(ans, can_buy)
    elif 10**d <= can_buy:
        ans = max(ans, 10**d - 1)

print(ans)
