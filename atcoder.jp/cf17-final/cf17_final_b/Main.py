s = input()
cnt = [0, 0, 0]
for i in "abc":
    cnt[ord(i) - 97] = s.count(i)

if max(cnt)-min(cnt)<=1:
    print("YES")
else:
    print("NO")
