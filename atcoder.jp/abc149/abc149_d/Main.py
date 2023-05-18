n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

d = {"r": p, "s": r, "p": s}
ans = 0
for i in range(n):
    if i - k < 0 or (0 <= i - k and t[i - k] != t[i]):
        ans += d[t[i]]
    else:
        t[i] = "."

print(ans)
