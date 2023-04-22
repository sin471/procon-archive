n = int(input())
s = input()

if len(set(s)) == 1:
    print(-1)
    exit()

c = 0
ans = 0
for i in range(n):
    if s[i] == "o":
        c += 1
    else:
        c = 0
    ans = max(c, ans)

print(ans)
