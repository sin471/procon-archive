s=input()
t=input()

ans="Yes"
for i in range(1,len(s)):
    if s[i-1]!=t[i-1]:
        if s[i-1]==t[i] and s[i]==t[i-1]:
            break
        else:
            ans="No"
            break

print(ans)