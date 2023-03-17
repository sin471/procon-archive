s = input()
chars = set(s)

ans = float("INF")
for char in chars:
    cnt = 0
    s2 = s
    while len(set(s2)) != 1:
        l = []
        for i in range(len(s2) - 1):
            if s2[i] == char or s2[i + 1] == char:
                l.append(char)
            else:
                l.append(".")
                
        s2 = "".join(l)
        cnt += 1
    ans = min(cnt, ans)

print(ans)
