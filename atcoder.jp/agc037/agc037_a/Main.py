s = input()
n = len(s)
i = 0
cnt = 0
is_2 = False
while i <= n-1:
    if i<=n-2 and s[i] == s[i + 1] and not is_2:
        i += 2
        is_2 = True
    else:
        i += 1
        is_2=False
        
    cnt += 1

print(cnt)
