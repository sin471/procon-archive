n = int(input())
s = input()

r_e = s.count("E")
l_w = 0
ans=float("INF")

for i in range(n):
    if i - 1 >= 0 and s[i - 1] == "W":
        l_w += 1
    if s[i] == "E":
        r_e -= 1
    ans = min(ans,r_e + l_w)

print(ans)
