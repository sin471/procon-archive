n = int(input())
s = [sorted(input()) for _ in range(n)]
s.sort()
s += [""]
m = len(s)

cnt = 0
t = s[0]
ans = 0

for i in range(m):
    if s[i] == t:
        cnt += 1
    else:
        t = s[i]
        if cnt >= 2:
            ans += (cnt * (cnt - 1)) // 2
        cnt = 1

print(ans)
