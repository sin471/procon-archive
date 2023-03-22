s = input()
n = len(s)

ans = 0
for i in range(n):
    if s[i] == "U":
        ans += i * 2 + (n - i - 1)
    elif s[i] == "D":
        ans += i + (n - i - 1) * 2

print(ans)
