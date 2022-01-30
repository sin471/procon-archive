s = list(input())

r_s = reversed(s)

cnt1 = 0
for i in s:
    if i == "a":
        cnt1 += 1
    else:
        break

cnt2 = 0
for i in r_s:
    if i == "a":
        cnt2 += 1
    else:
        break

for i in range(cnt2-cnt1):
    s.pop(-1)

print("Yes" if s == s[::-1] else "No")
