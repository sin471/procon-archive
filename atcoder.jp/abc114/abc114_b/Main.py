s = input()

ans = float("INF")

for i in range(3, len(s)+1):
    x = int(s[i-3:i])
    ans = min(abs(753-x), ans)


print(ans)
