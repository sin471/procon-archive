s = list(map(ord, list(input())))
t = list(map(ord, list(input())))

k = t[0]-s[0]
if k<0:
    k+=26
ans = "Yes"

for i, j in zip(s, t):
    if j-i == k or j-i+26==k:
        continue
    else:
        ans = "No"
        break

print(ans)
